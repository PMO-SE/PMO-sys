from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        res = (obj.owner == request.user)

        # Write permissions are only allowed to the owner of the snippet.
        print("user", request.user)
        print('owner', obj.owner)
        return res
