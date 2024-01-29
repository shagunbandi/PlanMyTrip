from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Accomodation
from .serializers import create_accomodation_serializer


class AccomodationViewSet(viewsets.ModelViewSet):
    queryset = Accomodation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        day_id = self.kwargs.get("day_id", None)
        return Accomodation.objects.filter(user=user, day__id=day_id)

    def get_serializer_class(self):
        day_id = self.kwargs.get("day_id", None)
        return create_accomodation_serializer(day_id=day_id, user=self.request.user)


class MoveAccomodationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, day_id, accomodation_id, method):
        user = request.user
        accomodation = get_object_or_404(
            Accomodation, id=accomodation_id, day__id=day_id, user=user
        )

        if method == "up":
            accomodation.up()
        elif method == "down":
            accomodation.down()
        else:
            return Response(
                {"detail": "Invalid method parameter"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
