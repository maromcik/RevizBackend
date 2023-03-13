from django.db import models
from django.contrib.auth.models import User


class Facility(models.Model):
    id = models.AutoField(primary_key=True)
    facility_name = models.CharField(max_length=100)
    facility_location = models.CharField(max_length=50)
    facility_building = models.CharField(max_length=50)

    def __str__(self):
        return self.facility_name

    def __unicode__(self):
        return self.facility_name

    class Meta:
        verbose_name_plural = "facilities"


class Year(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.year)

    def __unicode__(self):
        return str(self.year)

    class Meta:
        verbose_name_plural = "years"


class Cord(models.Model):
    id = models.AutoField(primary_key=True)
    cord_type = models.CharField(max_length=255)
    length = models.DecimalField(max_digits=8, decimal_places=2)
    separable = models.BooleanField()

    def __str__(self):
        return self.cord_type + " " + str(self.length) + " " + "m"

    def __unicode__(self):
        return self.cord_type + " " + str(self.length) + " " + "m"

    class Meta:
        verbose_name_plural = "cords"


class Voltage(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

    def __unicode__(self):
        return str(self.value)

    class Meta:
        verbose_name_plural = "voltages"


class DeviceTemplate(models.Model):
    TYPE_CHOICES = (
        ('Spotrebič', 'Spotrebič'),
        ('Predlžovačka', 'Predlžovačka')
    )

    CLASS = (
        ('1', '1'),
        ('2', '2')
    )

    USE_GROUP = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )

    OPERABILITY_CHOICES = (
        ('držané v ruke', 'držané v ruke'),
        ('prenosné', 'prenosné'),
        ('pripevnené, neprenosné','pripevnené, neprenosné')
    )

    id = models.AutoField(primary_key=True)
    device_type = models.CharField(max_length=127, choices=TYPE_CHOICES)
    device_name = models.CharField(max_length=255)
    device_class = models.CharField(max_length=10, choices=CLASS)
    use_group = models.CharField(max_length=10, choices=USE_GROUP)
    device_operability = models.CharField(max_length=255, choices=OPERABILITY_CHOICES, default='prenosné')

    def __str__(self):
        return self.device_name

    def __unicode__(self):
        return self.device_name

    class Meta:
        verbose_name_plural = "device templates"
   

class Device(models.Model):
    # fields of the table
    id = models.AutoField(primary_key=True)
    device_template = models.ForeignKey(DeviceTemplate, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True)
    device_SN = models.CharField(max_length=255)
    cord = models.ForeignKey(Cord, on_delete=models.CASCADE)
    device_voltage = models.ForeignKey(Voltage, on_delete=models.CASCADE)
    power = models.DecimalField(max_digits=16, decimal_places=4)
    current = models.DecimalField(max_digits=16, decimal_places=4)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True, blank=True)
    qr_text = models.CharField(max_length=255)

    # display names
    def __str__(self):
        return self.device_template.device_name

    def __unicode__(self):
        return self.device_template.device_name

    # display name of plural forms
    class Meta:
        verbose_name_plural = "devices"
