# drf_simplepermissions

This is a simple class to handle permissions in a Django application. It allows
you to list permissions as a tuple, list or string without writing custom
classes for each exception.

# Usage

```python
from drf_simplepermissions import SimplePermissions
from rest_framework import generics


class SimpleView(generics.GenericAPIView):
  serializer_class = ...
  permission_classes = (SimplePermissions,)
  allowed_permissions = ('codename_x', 'codename_y')

  def get(self, request, format=None):
    ...
```

It also includes a simple `is_demo()`-method which can be used to check if
views or other methods should be running in demo mode.

```python
from drf_simplepermissions import is_demo

if is_demo(User, demo_group='demo'):
  # We should run in demo mode when the user is in 'demo'

if is_demo(User, demo_mode=True):
  # We should run in demo mode as it's set globally
```

# Installation

Not documented yet.
