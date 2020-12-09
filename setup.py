from setuptools import setup

setup(name='drf-simplepermissions',
      version='0.0.4',
      description='SimplePermissions checks against a list of permissions',
      url='https://github.com/bellmann/python-drf-simplepermissions',
      author='Bellmann BV',
      author_email='opensource@bellmann.nl',
      packages=['drf_simplepermissions'],
      install_requires=[
          'django',
          'djangorestframework',
      ],
      python_requires='>=3.4',
      zip_safe=False)
