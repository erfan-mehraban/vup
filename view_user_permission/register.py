registered_views = []

def register_view(view_class):
    print(view_class, "registered")
    registered_views.append(view_class.__name__)
    return view_class