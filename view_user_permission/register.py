from .permissions import UserPermission
registered_views = []

def register_view(view_class):
    """
    register view in registered_views list and adding vup permission to view permission_classes
    """
    view_class.permission_classes.append(UserPermission)
    registered_views.append(get_view_name(view_class))
    return view_class

def get_view_name(view_class):
    """ combine app name and view name """
    return view_class.__module__+"."+view_class.__name__