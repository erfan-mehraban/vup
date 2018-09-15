def get_view_name(view_class):
    """ combine app name and view name """
    return view_class.__module__+"."+view_class.__name__