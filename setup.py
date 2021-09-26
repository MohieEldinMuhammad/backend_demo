from setuptools import setup

setup(
   name='backend_demo',
   version='0.0.1',
   description='backend demo',
   author='',
   author_email='no-one@ogoul.com',
   packages=['backend_demo'],
   install_requires=[
       'flask',
       'gunicorn',
       'nginx',
       'supervisor'
   ]
)
