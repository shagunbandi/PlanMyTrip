from plan.models.plan import Plan
from plan.serializers.plan import PlanSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)
