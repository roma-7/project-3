from rest_framework import permissions


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self,request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class CheckMovie(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'simple' and obj.status_movie == 'simple':
            return True
        elif request.user.status == 'pro':
            return True
        return False


class CheckHistory(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
