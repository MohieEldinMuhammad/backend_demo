from setuptools import setup

setup(
   name='mvse',
   version='0.0.1',
   description='backend demo',
   author='',
   author_email='no-one@ogoul.com',
   packages=['mvse'],
   install_requires=[
       'flask',
      'gunicorn',
     'nginx',
     'supervisor'
   ]
)
