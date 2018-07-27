from django.test import TestCase
from drf_simplepermissions import SimplePermissions


class View:
    pass


class Request:
    def __init__(self):
        self.user = None


class User:
    def __init__(self, permissions):
        self.permissions = permissions

    def has_perm(self, permission):
        if permission in self.permissions:
            return True


class TestPermissions(TestCase):
    def setUp(self):
        self.permissions = SimplePermissions()
        self.request = Request()
        self.view = View()

    def test_basic_tuple_permission(self):
        self.view.allowed_permissions = ('test',)
        self.request.user = User(permissions=('test',))
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), True) # noqa

    def test_incorrect_tuple_permission(self):
        self.view.allowed_permissions = ('test',)
        self.request.user = User(permissions=('test2',))
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), False) # noqa

    def test_basic_list_permission(self):
        self.view.allowed_permissions = ['test', ]
        self.request.user = User(permissions=('test',))
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), True) # noqa

    def test_incorrect_list_permission(self):
        self.view.allowed_permissions = ['test', ]
        self.request.user = User(permissions=('test2',))
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), False) # noqa

    def test_basic_string_permission(self):
        self.view.allowed_permissions = 'test'
        self.request.user = User(permissions=('test',))
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), True) # noqa

    def test_incorrect_string_permission(self):
        self.view.allowed_permissions = 'test'
        self.request.user = User(permissions=('test2',))
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), False) # noqa
