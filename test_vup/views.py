from rest_framework.viewsets import ModelViewSet
from .serializers import TestSerializer
from .models import Number
from view_user_permission.register import register_view

@register_view
class TestViewSet(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Number.objects.all()