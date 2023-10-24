from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Accomodation
from .serializers import create_accomodation_serializer


class AccomodationViewSet(viewsets.ModelViewSet):
    queryset = Accomodation.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        day_id = self.request.GET.get("day_id", None)
        return Accomodation.objects.filter(user=user, day__id=day_id)

    def get_serializer_class(self):
        day_id = self.request.GET.get("day_id", None)
        return create_accomodation_serializer(day_id=day_id, user=self.request.user)
