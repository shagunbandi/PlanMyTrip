from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Experience
from .serializers import ExperienceSerializer


class ExperienceListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the experiences for given requested user
        """
        experiences = Experience.objects.filter(user=request.user.id)
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create a new Experience
        """
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "type": request.data.get("type"),
            "google_place_id": request.data.get("google_place_id"),
            "ticket_link": request.data.get("ticket_link"),
            "reservation_link": request.data.get("reservation_link"),
            "activity_start_time": request.data.get("activity_start_time"),
            "activity_end_time": request.data.get("activity_end_time"),
            "order": request.data.get("order"),
            "itinerary": request.data.get("itinerary"),
            "user": request.user.id,
        }
        serializer = ExperienceSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExperienceDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    errors = {"experience_does_not_exist": "Object with experience id does not exists"}

    # 3. Retrieve
    def get(self, request, experience_id, *args, **kwargs):
        """
        Retrieves the Experience with given experience_id
        """
        experience_instance = self._get_object(experience_id, request.user.id)
        if not experience_instance:
            return Response(
                {"res": self.errors["experience_does_not_exist"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ExperienceSerializer(experience_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, experience_id, *args, **kwargs):
        """
        Updates the experience with given experience_id if exists
        """
        experience_instance = self._get_object(experience_id, request.user.id)
        if not experience_instance:
            return Response(
                {"res": self.errors["experience_does_not_exist"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "type": request.data.get("type"),
            "google_place_id": request.data.get("google_place_id"),
            "ticket_link": request.data.get("ticket_link"),
            "reservation_link": request.data.get("reservation_link"),
            "activity_start_time": request.data.get("activity_start_time"),
            "activity_end_time": request.data.get("activity_end_time"),
            "order": request.data.get("order"),
            "itinerary": request.data.get("itinerary"),
            "user": request.user.id,
        }
        serializer = ExperienceSerializer(
            instance=experience_instance, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, experience_id, *args, **kwargs):
        """
        Deletes the experience with given experience_id if exists
        """
        experience_instance = self._get_object(experience_id, request.user.id)
        if not experience_instance:
            return Response(
                {"res": self.errors["experience_does_not_exist"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        experience_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_object(self, experience_id, user_id):
        """
        Helper method to get the object with given experience_id, and user_id
        """
        try:
            return Experience.objects.get(id=experience_id, user=user_id)
        except Experience.DoesNotExist:
            return None
