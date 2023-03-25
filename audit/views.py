import datetime

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *

delay = 1000


def get_unix_ms(o):
    return o.modified.timestamp() * 1000


def generate_devices():
    for i in range(10000):
        d = Device.objects.create(room=Room.objects.get(id=1),
                                  audit_no=i,
                                  device_model=DeviceModel.objects.get(id=1),
                                  device_SN='0',
                                  cord=Cord.objects.get(id=1),
                                  device_voltage=Voltage.objects.get(id=1),
                                  power=0,
                                  current=0,
                                  year=Year.objects.get(id=1),
                                  qr_text='0',
                                  note='0')
        d.save()


def remove_all():
    Device.objects.all().delete()


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


@api_view(['POST'], )
@permission_classes([AllowAny], )
def push_cords(request):
    cords = []
    data = request.data
    for element in data:
        if Cord.objects.filter(id=element['id']).exists():
            cord = Cord.objects.get(id=element['id'])
            if int(element['modified']) - get_unix_ms(cord) > delay:
                cord.cord_type = element['cord_type']
                cord.length = element['length']
                cord.separable = element['separable']
        else:
            cord = Cord.objects.create(cord_type=element['cord_type'],
                                       length=element['length'],
                                       separable=element['separable'])
        cord.save()
        cords.append(cord)
    return Response(CordSerializer(cords, many=True).data)


@api_view(['POST'], )
@permission_classes([AllowAny], )
def push_device_manufacturers(request):
    manufacturers = []
    data = request.data
    for element in data:
        if DeviceManufacturer.objects.filter(id=element['id']).exists():
            manufacturer = DeviceManufacturer.objects.get(id=element['id'])
            if int(element['modified']) - get_unix_ms(manufacturer) > delay:
                manufacturer.name = element['name']
        else:
            manufacturer = DeviceManufacturer.objects.create(name=element['name'])
        manufacturer.save()
        manufacturers.append(manufacturer)
    return Response(DeviceManufacturerSerializer(manufacturers, many=True).data)


@api_view(['POST'], )
@permission_classes([AllowAny], )
def push_devices(request):
    devices = []
    data = request.data
    for element in data:
        if Device.objects.filter(id=element['id']).exists():
            device = Device.objects.get(id=element['id'])
            if int(element['modified']) - get_unix_ms(device) > delay:
                device.room = Room.objects.get(pk=element['room'])
                device.audit_no = element['audit_no']
                device.device_model = DeviceModel.objects.get(pk=element['device_model'])
                device.device_SN = element['device_SN']
                device.cord = Cord.objects.get(pk=element['cord'])
                device.device_voltage = Voltage.objects.get(pk=element['device_voltage'])
                device.power = element['power']
                device.current = element['current']
                device.year = Year.objects.get(pk=element['year'])
                device.qr_text = element['qr_text']
                device.note = element['note']

        else:
            device = Device.objects.create(room=Room.objects.get(pk=element['room']),
                                           audit_no=element['audit_no'],
                                           device_model=DeviceModel.objects.get(pk=element['device_model']),
                                           device_SN=element['device_SN'],
                                           cord=Cord.objects.get(pk=element['cord']),
                                           device_voltage=Voltage.objects.get(pk=element['device_voltage']),
                                           power=element['power'],
                                           current=element['current'],
                                           year=Year.objects.get(pk=element['year']),
                                           qr_text=element['qr_text'],
                                           note=element['note'],
                                           )
        device.save()
        devices.append(device)

    return Response(DeviceSerializer(devices, many=True).data)


@api_view(['POST'], )
@permission_classes([AllowAny], )
def push_device_models(request):
    models = []
    data = request.data
    for element in data:
        if DeviceModel.objects.filter(id=element['id']).exists():
            model = DeviceModel.objects.get(id=element['id'])
            if int(element['modified']) - get_unix_ms(model) > delay:
                model.device_name = element['device_name']
                model.device_type = DeviceType.objects.get(pk=element['device_type'])
                model.device_category = DeviceCategory.objects.get(pk=element['device_category'])
                model.device_manufacturer = DeviceManufacturer.objects.get(pk=element['device_manufacturer'])
                model.device_class = DeviceClass.objects.get(pk=element['device_class'])
                model.use_group = DeviceUseGroup.objects.get(pk=element['use_group'])
                model.mode_of_operation = DeviceModeOfOperation.objects.get(pk=element['mode_of_operation'])
        else:
            model = DeviceModel.objects.create(device_name=element['device_name'],
                                               device_type=DeviceType.objects.get(pk=element['device_type']),
                                               device_category=DeviceCategory.objects.get(
                                                   pk=element['device_category']),
                                               device_manufacturer=DeviceManufacturer.objects.get(
                                                   pk=element['device_manufacturer']),
                                               device_class=DeviceClass.objects.get(pk=element['device_class']),
                                               use_group=DeviceUseGroup.objects.get(pk=element['use_group']),
                                               mode_of_operation=DeviceModeOfOperation.objects.get(pk=element['mode_of_operation']))
            model.save()
            models.append(model)

    return Response(DeviceModelSerializer(models, many=True).data)


@api_view(['POST'], )
@permission_classes([AllowAny], )
def push_rooms(request):
    rooms = []
    data = request.data
    for element in data:
        if Room.objects.filter(id=element['id']).exists():
            room = Room.objects.get(id=element['id'])
            if int(element['modified']) - get_unix_ms(room) > delay:
                room.room = element['room']
                room.branch = Branch.objects.get(pk=element['branch'])
        else:
            room = Room.objects.create(room=element['room'], branch=Branch.objects.get(pk=element['branch']))
        room.save()
        rooms.append(room)

    return Response(RoomSerializer(rooms, many=True).data)


@api_view(['POST'], )
@permission_classes([AllowAny], )
def push_voltages(request):
    voltages = []
    data = request.data
    for element in data:
        if Voltage.objects.filter(id=element['id']).exists():
            voltage = Voltage.objects.get(id=element['id'])
            if int(element['modified']) - get_unix_ms(voltage) > delay:
                voltage.value = element['value']
        else:
            voltage = Voltage.objects.create(value=element['value'])
        voltage.save()
        voltages.append(voltage)
    return Response(VoltageSerializer(voltages, many=True).data)


@api_view(['POST'], )
@permission_classes([AllowAny], )
def push_years(request):
    years = []
    data = request.data
    for element in data:
        if Year.objects.filter(id=element['id']).exists():
            year = Year.objects.get(id=element['id'])
            if int(element['modified']) - get_unix_ms(year) > delay:
                year.year = element['year']
        else:
            year = Year.objects.create(year=element['year'])
        year.save()
        years.append(year)

    return Response(YearSerializer(years, many=True).data)
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
