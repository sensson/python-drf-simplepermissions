from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import permissions
from drf_simplepermissions.exceptions import SimpleModeException


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


def is_demo(user, demo_group='demo'):
    '''is_demo checks if a user is added to a demo group or groups. If a
    list of groups is supplied, it will try to match against any group and
    if a match is found, it will return true.

    Global demo mode can be enabled by changing `settings.DEMO` to True. If
    it's set to False you can override it by adding users to a group. You
    can't override `settings.DEMO` when it's set to True.

    This allows you to setup demo accounts that are restricted in what they
    can do or what they can see. Keep in mind that it is not intended to
    be used as a permission_classes' class as that has a different purpose.'''

    try:
        basestring
    except NameError:
        basestring = str

    if hasattr(settings, 'DEMO'):
        if not isinstance(settings.DEMO, bool):
            raise SimpleModeException('DEMO {0} is unsupported'.format(
                settings.DEMO,
            ))

        if settings.DEMO:
            return settings.DEMO

    if isinstance(user, User):
        if isinstance(demo_group, basestring):
            return user.groups.filter(name=demo_group).exists()

        if isinstance(demo_group, (list)):
            return user.groups.filter(name__in=demo_group).exists()

    return False
