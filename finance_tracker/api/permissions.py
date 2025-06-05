from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
        Custom permission to allow only the resource owner or an admin to access.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.owner == request.user