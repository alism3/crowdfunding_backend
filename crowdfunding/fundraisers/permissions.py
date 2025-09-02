from rest_framework import permissions

class IsOwnerOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): #obj can really be many things
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user
        
class IsSupporterOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): #obj can really be many things
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.supporter == request.user
