from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import RelatedField
from .models import *


class DeviceTemplateSerializer(ModelSerializer):
    class Meta:
        model = DeviceTemplate
        fields = ['device_type', 'device_name', 'device_class', 'device_operability']


class DeviceSerializer(ModelSerializer):
    # template = DeviceTemplateSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = ['device_template', 'facility', 'device_SN', 'cord', 'device_voltage', 'power', 'current', 'qr_text']


class FacilitySerializer(ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"
