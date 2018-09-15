from .permissions import UserPermission
from .helper import get_view_name
registered_views = []

def register_view(view_class):
    """
    register view in registered_views list and adding vup permission to view permission_classes
    """
    if isinstance(view_class.permission_classes, tuple):
        raise ValueError(f"permission_classes of {view_class.__name__} must be list")
    view_class.permission_classes.append(UserPermission)
    registered_views.append(get_view_name(view_class))
    return view_class
