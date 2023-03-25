from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import RelatedField
from .models import *


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class YearSerializer(ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"


class CordSerializer(ModelSerializer):
    class Meta:
        model = Cord
        fields = "__all__"


class VoltageSerializer(ModelSerializer):
    class Meta:
        model = Voltage
        fields = "__all__"


class DeviceTypeSerializer(ModelSerializer):
    class Meta:
        model = DeviceType
        fields = "__all__"


class DeviceModeOfOperationSerializer(ModelSerializer):
    class Meta:
        model = DeviceModeOfOperation
        fields = "__all__"


class DeviceManufacturerSerializer(ModelSerializer):
    class Meta:
        model = DeviceManufacturer
        fields = "__all__"


class DeviceCategorySerializer(ModelSerializer):
    class Meta:
        model = DeviceCategory
        fields = "__all__"


class DeviceUseGroupSerializer(ModelSerializer):
    class Meta:
        model = DeviceUseGroup
        fields = "__all__"


class DeviceClassSerializer(ModelSerializer):
    class Meta:
        model = DeviceClass
        fields = "__all__"


class DeviceModelSerializer(ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = '__all__'


class DeviceSerializer(ModelSerializer):
    # dm = DeviceModelSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'
