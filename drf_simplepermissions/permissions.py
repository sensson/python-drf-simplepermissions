from rest_framework import permissions


class SimplePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            basestring
        except NameError:
            basestring = str

        if isinstance(view.allowed_permissions, (list, tuple)):
            for permission in view.allowed_permissions:
                if request.user.has_perm(permission):
                    return True

        if isinstance(view.allowed_permissions, basestring):
            if request.user.has_perm(view.allowed_permissions):
                return True

        return False
