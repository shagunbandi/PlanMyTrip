from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to perform CRUD operations.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the requesting user is the owner of the object.
        return obj.owner == request.user
