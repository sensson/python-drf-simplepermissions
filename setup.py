from setuptools import setup

setup(name='drf_simplepermissions',
      version='0.0.1',
      description='SimplePermissions checks against a list of permissions',
      url='https://git.sensson.net/bellmann/python-drf-simplepermissions',
      author='Bellmann BV',
      author_email='ton@bellmann.nl',
      packages=['drf_simplepermissions'],
      install_requires=[
          'django',
          'djangorestframework',
      ],
      zip_safe=False)
