from django.db import models
from django.contrib.auth.models import User


class Facility(models.Model):
    facilityName = models.CharField(max_length=100)
    facilityLocation = models.CharField(max_length=50)

    def __str__(self):
        return self.facilityName

    def __unicode__(self):
        return self.facilityName

    class Meta:
        verbose_name_plural = "facilities"


class Device(models.Model):
    # fields of the table
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True)
    deviceName = models.CharField(max_length=100)
    qrText = models.CharField(max_length=250)

    # display names
    def __str__(self):
        return self.deviceName

    def __unicode__(self):
        return self.deviceName

    # display name of plural forms
    class Meta:
        verbose_name_plural = "devices"
