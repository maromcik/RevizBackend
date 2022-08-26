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
    # field options
    list_display = ['deviceName', 'qrText', 'facility']
    list_filter = ['deviceName', 'facility']
    search_fields = ['deviceName', 'facility__facilityName']


class FacilityAdmin(admin.ModelAdmin):
    # field options
    list_display = ['facilityName', 'facilityLocation']
    list_filter = ['facilityName', 'facilityLocation']
    search_fields = ['facilityName', 'facilityLocation']

# registers all the models
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Person, PersonAdmin)
# admin.site.register(Log, LogAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Device, DeviceAdmin)
# admin.site.register(SubscriptionInfo)
admin.site.site_header = "Reviz Administration"