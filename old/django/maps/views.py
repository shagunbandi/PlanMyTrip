from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utilities import google_distance_matrix
from .serializers import DistanceBetweenPlacesRequestSerializer

# from .models import Item
# from .serializers import ItemSerializer
# from django.shortcuts import get_object_or_404
# from rest_framework import serializers
# from rest_framework import status


@api_view(["GET"])
def MapsOverview(request):
    maps_url = {
        "all_items": "/",
        "Search by Category": "/?category=category_name",
        "Search by Subcategory": "/?subcategory=category_name",
        "Add": "/create",
        "Update": "/update/pk",
        "Delete": "/item/pk/delete",
    }

    return Response(maps_url)


@api_view(["POST"])
def distance_with_place_ids(request):
    content = request.data
    DistanceBetweenPlacesRequestSerializer(data=request.data).is_valid()

    origin_place_id = content.get("origin_place_id")
    destination_place_id = content.get("destination_place_id")
    mode = content.get("mode", "driving")

    response = google_distance_matrix(
        origin_place_id,
        destination_place_id,
        mode,
    )
    return Response(response, 200)
