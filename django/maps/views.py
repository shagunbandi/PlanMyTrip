from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utilities import google_distance_matrix
from .serializers import DistanceBetweenPlacesRequestSerializer


@api_view(["POST"])
def distance_with_place_ids(request):
    request_serialiser = DistanceBetweenPlacesRequestSerializer(data=request.data)
    origin_place_id = request_serialiser.data.get("origin_place_id")
    destination_place_id = request_serialiser.data.get("destination_place_id")
    mode = request_serialiser.data.get("mode", "driving")

    response = google_distance_matrix(
        origin_place_id,
        destination_place_id,
        mode,
    )
    return Response(response, 200)
