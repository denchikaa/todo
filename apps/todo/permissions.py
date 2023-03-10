from rest_framework import permissions


class IsOwnerPermissions(permissions.BasePermissions):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user.pk == request.user.pk)