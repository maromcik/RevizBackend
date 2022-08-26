from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *

@api_view(['GET'],)
@permission_classes([AllowAny],)
def get_devices(request):
    devices = Device.objects.all()
    return Response(DeviceSerializer(reversed(devices[max(len(devices)-100, 0):]), many=True).data)


@api_view(['GET'],)
@permission_classes([AllowAny],)
def get_devices_by_facility(request, facility_name):
    devices = Device.objects.filter(facility__facilityName=facility_name)
    return Response(DeviceSerializer(reversed(devices[max(len(devices)-100, 0):]), many=True).data)


@api_view(['PUT'],)
@permission_classes([AllowAny],)
def update_device(request, qr):
    device = Device.objects.get(qrText=qr)
    serializer = DeviceSerializer(device, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'],)
@permission_classes([AllowAny],)
def create_device(request):
    data = request.data
    device = Device.objects.create(
        facility=Facility.objects.get(pk=data['facility']),
        deviceName=data['deviceName'],
        qrText=data['qrText'],
    )
    serializer = DeviceSerializer(device, many=False)
    return Response(serializer.data)


@api_view(['DELETE'],)
@permission_classes([AllowAny],)
def delete_device(request, qr):
    device = Device.objects.get(qrText=qr)
    device.delete()
    return Response("Device was deleted!")


@api_view(['GET'],)
@permission_classes([AllowAny],)
def get_device(request, qr):
    return Response(DeviceSerializer(Device.objects.get(qrText=qr), many=False).data)


@api_view(['GET'],)
@permission_classes([AllowAny],)
def get_facilities(request):
    return Response(FacilitySerializer(Facility.objects.all(), many=True).data)


@api_view(['GET'],)
@permission_classes([AllowAny],)
def get_facility_by_name(request, facility_name):
    return Response(FacilitySerializer(Facility.objects.get(facilityName=facility_name), many=False).data)