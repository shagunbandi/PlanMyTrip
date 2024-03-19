from common.serializers import CreateSerializer
from plan.models.plan import Plan
from plan.serializers.agenda import AgendaSerializer
from plan.serializers.place import PlaceSerializer


class PlanSerializer(CreateSerializer):
    agendas = AgendaSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = [
            "id",
            "title",
            "agendas",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
        ]
