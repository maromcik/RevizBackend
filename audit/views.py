from django.http import Http404
from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from .exceptions.CreateDeviceException import *
from .exceptions.UpdateDeviceException import *


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_cities(request):
    return Response(CitySerializer(City.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_locations(request):
    return Response(LocationSerializer(Location.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_companies(request):
    return Response(CompanySerializer(Company.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_branches(request):
    return Response(BranchSerializer(Branch.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_rooms(request):
    return Response(RoomSerializer(Room.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_year(request):
    return Response(YearSerializer(Year.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_cords(request):
    return Response(CordSerializer(Cord.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_voltages(request):
    return Response(VoltageSerializer(Voltage.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_device_types(request):
    return Response(DeviceTypeSerializer(DeviceType.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_device_mode_operations(request):
    return Response(DeviceModeOfOperationSerializer(DeviceModeOfOperation.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_device_manufacturers(request):
    return Response(DeviceManufacturerSerializer(DeviceManufacturer.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_device_categories(request):
    return Response(DeviceCategorySerializer(DeviceCategory.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_device_use_groups(request):
    return Response(DeviceUseGroupSerializer(DeviceUseGroup.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_device_classes(request):
    return Response(DeviceClassSerializer(DeviceClass.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_models(request):
    return Response(DeviceModelSerializer(DeviceModel.objects.all(), many=True).data)


@api_view(['GET'], )
@permission_classes([AllowAny], )
def get_devices(request):
    return Response(DeviceSerializer(Device.objects.all(), many=True).data)

# @api_view(['GET'],)
# @permission_classes([AllowAny],)
# def get_devices_by_facility(request, facility_name):
#     devices = Device.objects.filter(facility__facility_name=facility_name)
#     return Response(DeviceSerializer(reversed(devices[max(len(devices)-100, 0):]), many=True).data)
#

# @api_view(['PUT'],)
# @permission_classes([AllowAny],)
# def update_device(request, qr):
#     if not device_exists(qr):
#         raise UpdateDeviceNotExistsException()
#     device = Device.objects.get(qr_text=qr)
#     data = request.data
#     if device_exists(data['qr_text']) and (qr != data['qr_text']):
#         raise UpdateDeviceDuplicitQRException()
#
#     serializer = DeviceSerializer(device, data=data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['POST'],)
# @permission_classes([AllowAny],)
# def create_device(request):
#     data = request.data
#     if data['qr_text'] == "":
#         raise CreateDeviceEmptyQRException()
#     if device_exists(data['qr_text']):
#         raise CreateDeviceExistsException()
#     device = Device.objects.create(
#         facility=Facility.objects.get(pk=data['facility']),
#         device_template=DeviceModel.objects.get(pk=data['device_template']),
#         device_SN=data['device_SN'],
#         cord=Cord.objects.get(pk=data['cord']),
#         device_voltage=Voltage.objects.get(pk=data['device_voltage']),
#         power=data['power'],
#         current=data['current'],
#         qr_text=data['qr_text'],
#     )
#     serializer = DeviceSerializer(device, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'],)
# @permission_classes([AllowAny],)
# def delete_device(request, qr):
#     device = Device.objects.get(qr_text=qr)
#     device.delete()
#     return Response("Device was deleted!")
#
#
# @api_view(['GET'],)
# @permission_classes([AllowAny],)
# def get_device(request, qr):
#     try:
#         return Response(DeviceSerializer(Device.objects.get(qr_text=qr), many=False).data)
#     except Device.DoesNotExist:
#         raise Http404
#
#
# @api_view(['GET'],)
# @permission_classes([AllowAny],)
# def get_facilities(request):
#     return Response(FacilitySerializer(Facility.objects.all(), many=True).data)
#
#
# @api_view(['GET'],)
# @permission_classes([AllowAny],)
# def get_facility_by_name(request, facility_name):
#     return Response(FacilitySerializer(Facility.objects.get(facility_name=facility_name), many=False).data)
#
#
# def device_exists(qr):
#     return Device.objects.filter(qr_text=qr).exists()
