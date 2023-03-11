from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from audit.models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import path
from audit import views
from django.http import HttpResponseRedirect
from django.contrib import messages


# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'qr_text', 'facility']
    list_filter = ['device_name', 'facility']
    search_fields = ['device_name', 'facility__facilityName']


class FacilityAdmin(admin.ModelAdmin):
    list_display = ['facility_name', 'facility_location', 'facility_building']
    list_filter = ['facility_name', 'facility_location', 'facility_building']
    search_fields = ['facility_name', 'facility_location', 'facility_building']


class CordAdmin(admin.ModelAdmin):
    list_display = ['cord_type', 'length', 'separable']
    list_filter = ['cord_type', 'length', 'separable']
    search_fields = ['cord_type', 'length', 'separable']


class DeviceTemplateAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'device_type', 'device_class', 'device_operability']
    list_filter = ['device_type', 'device_name', 'device_class', 'device_operability']
    search_fields = ['device_type', 'device_name', 'device_class', 'device_operability']


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_template', 'facility', 'device_SN', 'cord', 'device_voltage']
    search_fields =  ['device_template', 'facility', 'device_SN', 'qr_text']
    list_filter = ['device_template', 'facility', 'cord', 'device_voltage']


admin.site.register(Facility, FacilityAdmin)
admin.site.register(DeviceTemplate, DeviceTemplateAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Voltage)
admin.site.register(Cord, CordAdmin)
admin.site.site_header = "Reviz Administration"