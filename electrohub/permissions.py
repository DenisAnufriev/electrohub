from rest_framework import permissions


class IsUserModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsUserOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
