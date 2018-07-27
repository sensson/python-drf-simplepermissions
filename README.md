# drf_simplepermissions

This is a simple class to handle permissions in a DRF view. It allows you to
list permissions as a tuple, list or string without writing custom classes
for each exception.

```
from drf_simplepermissions import SimplePermissions
from rest_framework import generics


class SimpleView(generics.GenericAPIView):
  serializer_class = ...
  permission_classes = (SimplePermissions,)
  allowed_permissions = ('codename_x', 'codename_y')

  def get(self, request, format=None):
    ...
```

# Installation

Not documented yet.
