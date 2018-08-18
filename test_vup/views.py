from rest_framework.viewsets import ModelViewSet
from .serializers import TestSerializer
from .models import Number

class TestViewSet(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Number.objects.all()