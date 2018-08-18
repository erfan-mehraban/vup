from .permissions import UserPermission
registered_views = []

def register_view(view_class):
    """
    register view in registered_views list and adding vup permission to view permission_classes
    """
    view_class.permission_classes.append(UserPermission)
    registered_views.append(view_class.__name__)
    return view_class