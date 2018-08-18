from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Number

class TestSerializer(ModelSerializer):
    number = IntegerField

    class Meta:
        model = Number
        exclude = []
