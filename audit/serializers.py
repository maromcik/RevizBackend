from rest_framework.serializers import ModelSerializer
from .models import Device, Facility


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ['deviceName', 'qrText', 'facility']


class FacilitySerializer(ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"
