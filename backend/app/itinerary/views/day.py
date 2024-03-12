from common.exceptions import ValidationException
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from itinerary.models.day import Day
from itinerary.models.itinerary import Itinerary
from itinerary.serializers.day import DaySerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        itinerary = self._get_itinerary()
        return (
            super().get_queryset().filter(owner=self.request.user, itinerary=itinerary)
        )

    def perform_create(self, serializer):
        itinerary = self._get_itinerary()

        serializer.save(itinerary=itinerary)

    def _get_itinerary(self):
        itinerary_id = self.kwargs.get("itinerary_id")
        itinerary = get_object_or_404(
            Itinerary, pk=itinerary_id, owner=self.request.user
        )
        return itinerary


class MoveContentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, object_id):
        content_type = request.data.get("content_type", "")
        method = request.data.get("method", "")

        model_object = self.get_model_object(request, object_id, content_type)
        if method == "up":
            model_object.up()
        elif method == "down":
            model_object.down()

        # Update parent for place and put it in the last place
        elif method == "change-parent" and content_type == "place":
            parent_id = request.data.get("parent_id", 0)
            parent_content_type = request.data.get("parent_content_type", "")
            parent_object = self.get_model_object(
                request, parent_id, parent_content_type
            )
            model_object.parent = parent_object
            model_object.order = None
            model_object.save()
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_model_object(self, request, object_id, content_type):
        if content_type not in ["day", "place"]:
            raise ValidationException("Invalid content type.")
        model_class = (
            ContentType.objects.filter(model=content_type.lower()).first().model_class()
        )
        model_object = get_object_or_404(model_class, id=object_id, owner=request.user)
        return model_object
