from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Day
from .serializers import DaySerializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        return Day.objects.filter(user=user)
