# View User Permission

This tool controll and manage permissions of users to access to views in django rest api just like how django manage access of users to models.

See test app for how to use it

You can change and add permissions to groups and users in admin

# Getting started

## Installing


```bash
$ pip3 install git+https://github.com/erfan-mehraban/vup
```

And add ```view_user_permission``` to ```INSTALLED_APPS``` in django project setting:

```python3
INSTALLED_APPS = [
    ...
    'view_user_permission',
]
```

Then for applying megrations:

```bash
$ python3 manage.py migrate view_user_permission
```

## Registering views

### Applying for custom views

Only views wich has been registered in app will be controlled for permissions.

For registering views you need only use ```@register_view``` decorator:

```python3
from view_user_permission.register import register_view

@register_view
class SomeViewSet(ViewSet):
    ...
```

After defining view you should use manage command to add them to your databse. (like ```migrate``` command for applying models!):

```bash
$ python3 manage.py register_views
```
### Applying for all views

change the ```settings.py``` and modify ```DEFAULT_PERMISSION_CLASSES```:

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'view_user_permission.permissions.UserPermission',
        ...
    )
}
```

## Grouping and permission accessing

Groups consist of some users and permissions granted to groups. So you have to join your users to groups, in other word make a many-to-many (or 1-to-many) relationship from your users to groups.

Ensure field name should be `roles`.

```python3
class CustomUser(AbstractUser):
    roles = models.ManyToManyField('view_user_permission.Group')
```

Also dont forget to ```makemigrations``` for your project and ```migrate``` it!
_Note: you can change default user model to your custom user by changing ```AUTH_USER_MODEL``` in ```settings```_


## Test app

See ```test_vup``` app for more detail of implementation.
You can access [url]/admin for admin page and [url]/test for test view.

This test app only save a number and you can l/r/c/u/up it.

# Concept and desing

```@register_view``` append view in ```view_user_permission.register.registered_views```. Then ```register_views``` command make a permission instance for every view and actions.

Also ```@register_view``` append vup permssion to permission list of view. When user want to access view ```UserPermission.has_permission``` will be called and this function check user permission exsits according to loged in user, view and action requested.

# Other notes

## Built With

* [Django REST framework](http://www.django-rest-framework.org/)
* [setuptools](https://pypi.org/project/setuptools/) - Package Management
* [CityHash](https://opensource.googleblog.com/2011/04/introducing-cityhash.html) - hashing permissions for make efficient permission checking. 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## TODO

* bring roles relation in group admin page