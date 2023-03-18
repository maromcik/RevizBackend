from django.contrib import admin
from audit.models import *

# Register your models here.


# class FacilityAdmin(admin.ModelAdmin):
#     list_display = ['facility_name', 'facility_location', 'facility_building']
#     list_filter = ['facility_name', 'facility_location', 'facility_building']
#     search_fields = ['facility_name', 'facility_location', 'facility_building']

class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ['type', 'tag']
    list_filter = ['type', 'tag']
    search_fields = ['type', 'tag']


class CordAdmin(admin.ModelAdmin):
    list_display = ['cord_type', 'length', 'separable']
    list_filter = ['cord_type', 'length', 'separable']
    search_fields = ['cord_type', 'length', 'separable']


class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'device_type', 'device_class', 'use_group', 'mode_of_operation']
    list_filter = ['device_type', 'device_name', 'device_class', 'use_group', 'mode_of_operation']
    search_fields = ['device_type', 'device_name', 'device_class', 'use_group', 'mode_of_operation']


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_model', 'room', 'device_SN', 'cord', 'device_voltage']
    search_fields = ['device_model', 'room', 'device_SN', 'qr_text']
    list_filter = ['device_model', 'room', 'cord', 'device_voltage']


class CityAdmin(admin.ModelAdmin):
    list_display = ['city', 'zip_code']
    search_fields = ['city', 'zip_code']
    list_filter = ['city', 'zip_code']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['city', 'address']
    search_fields = ['city', 'address']
    list_filter = ['city', 'address']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['room', 'branch']
    search_fields = ['room', 'branch']
    list_filter = ['room', 'branch']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag']
    search_fields = ['name', 'tag']
    list_filter = ['name', 'tag']


class BranchAdmin(admin.ModelAdmin):
    list_display = ['company', 'branch', 'location', 'tag']
    search_fields = ['company', 'branch', 'location', 'tag']
    list_filter = ['company', 'branch', 'location', 'tag']


# admin.site.register(Facility, FacilityAdmin)
admin.site.register(DeviceModel, DeviceModelAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Voltage)
admin.site.register(Cord, CordAdmin)
admin.site.register(Year)
admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(DeviceClass)
admin.site.register(DeviceUseGroup)
admin.site.register(DeviceModeOfOperation)
admin.site.register(Room, RoomAdmin)
admin.site.register(DeviceCategory)
admin.site.register(DeviceManufacturer)
admin.site.site_header = "Reviz Administration"