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
            "timeline": request.data.get("timeline"),
            "user": request.user.id,
        }
        serializer = ItinerarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItineraryDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    errors = {"itinerary_does_not_exist": "Object with itinerary id does not exists"}

    # 3. Retrieve
    def get(self, request, itinerary_id, *args, **kwargs):
        """
        Retrieves the Itinerary with given itinerary_id
        """
        itinerary_instance = self._get_object(itinerary_id, request.user.id)
        if not itinerary_instance:
            return Response(
                {"res": self.errors["itinerary_does_not_exist"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ItinerarySerializer(itinerary_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, itinerary_id, *args, **kwargs):
        """
        Updates the itinerary with given itinerary_id if exists
        """
        itinerary_instance = self._get_object(itinerary_id, request.user.id)
        if not itinerary_instance:
            return Response(
                {"res": self.errors["itinerary_does_not_exist"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "timeline": request.data.get("timeline"),
            "user": request.user.id,
        }
        serializer = ItinerarySerializer(
            instance=itinerary_instance, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, itinerary_id, *args, **kwargs):
        """
        Deletes the itinerary with given itinerary_id if exists
        """
        itinerary_instance = self._get_object(itinerary_id, request.user.id)
        if not itinerary_instance:
            return Response(
                {"res": self.errors["itinerary_does_not_exist"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        itinerary_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_object(self, itinerary_id, user_id):
        """
        Helper method to get the object with given itinerary_id, and user_id
        """
        try:
            return Itinerary.objects.get(id=itinerary_id, user=user_id)
        except Itinerary.DoesNotExist:
            return None
