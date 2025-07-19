from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """Custom permission to only allow owners t edit or delete their objects."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or getattr(obj, 'host', None) == request.user
    