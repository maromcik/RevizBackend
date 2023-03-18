from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import RelatedField
from .models import *


class DeviceModelSerializer(ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = '__all__'
        depth = 5


class DeviceSerializer(ModelSerializer):
    # dm = DeviceModelSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'
        depth = 5

