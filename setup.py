from setuptools import setup, find_packages

setup(name='view_user_permission',
    version='0.2',
    description='checking view action permissions by user credinals',
    author='Erfan Mehraban',
    author_email='erfan.mehraban@gmail.com',
    license='MIT',
    packages=['view_user_permission', 'view_user_permission.migrations'],
    install_requires=[
        'cityhash==0.2.3.post9',
        'Django==2.1',
        'djangorestframework==3.8.2',
    ],
    include_package_data=True,
    zip_safe=False)