from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from drf_simplepermissions import SimplePermissions


class View:
    pass


class Request:
    def __init__(self):
        self.user = None


class TestPermissions(TestCase):
    def setUp(self):
        self.permissions = SimplePermissions()
        self.request = Request()
        self.view = View()

        # Create a user
        user = User.objects.create_user(username='demo', password='demo')
        user.save()
        self.request.user = user

        # Create a content_type to test with
        self.content_type = ContentType(app_label='test_case', model='permissions') # noqa
        self.content_type.save()

    def test_basic_tuple_permission(self):
        permission = Permission.objects.create(codename='test', content_type=self.content_type) # noqa
        self.request.user.user_permissions.add(permission)
        self.view.allowed_permissions = ('test_case.test',)
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), True) # noqa

    def test_incorrect_tuple_permission(self):
        permission = Permission.objects.create(codename='test2', content_type=self.content_type) # noqa
        self.request.user.user_permissions.add(permission)
        self.view.allowed_permissions = ('test_case.test',)
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), False) # noqa

    def test_basic_list_permission(self):
        permission = Permission.objects.create(codename='test', content_type=self.content_type) # noqa
        self.request.user.user_permissions.add(permission)
        self.view.allowed_permissions = ['test_case.test', ]
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), True) # noqa

    def test_incorrect_list_permission(self):
        permission = Permission.objects.create(codename='test2', content_type=self.content_type) # noqa
        self.request.user.user_permissions.add(permission)
        self.view.allowed_permissions = ['test_case.test', ]
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), False) # noqa

    def test_basic_string_permission(self):
        permission = Permission.objects.create(codename='test', content_type=self.content_type) # noqa
        self.request.user.user_permissions.add(permission)
        self.view.allowed_permissions = 'test_case.test'
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), True) # noqa

    def test_incorrect_string_permission(self):
        permission = Permission.objects.create(codename='test2', content_type=self.content_type) # noqa
        self.request.user.user_permissions.add(permission)
        self.view.allowed_permissions = 'test'
        self.assertEqual(self.permissions.has_permission(request=self.request, view=self.view), False) # noqa
