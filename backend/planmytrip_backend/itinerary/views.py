from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Itinerary
from .serializers import ItinerarySerializer


class ItineraryListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the itineraries for given requested user
        """
        itineraries = Itinerary.objects.filter(user=request.user.id)
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create a new Itinerary
        """
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "user": request.user.id,
        }
        serializer = ItinerarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
