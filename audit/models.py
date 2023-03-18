from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    def __str__(self):
        return self.city

    def __unicode__(self):
        return self.city

    class Meta:
        verbose_name_plural = "cities"


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.city.city + " " + self.address

    def __unicode__(self):
        return self.city.city + " " + self.address

    class Meta:
        verbose_name_plural = "locations"


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"


class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.company.name + " " + self.branch

    def __unicode__(self):
        return self.company.name + " " + self.branch

    class Meta:
        verbose_name_plural = "branches"


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    room = models.CharField(max_length=127)

    def __str__(self):
        return self.room

    def __unicode__(self):
        return self.room

    class Meta:
        verbose_name_plural = "rooms"


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


class DeviceType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    tag = models.CharField(max_length=10)

    def __str__(self):
        return str(self.type)

    def __unicode__(self):
        return str(self.type)

    class Meta:
        verbose_name_plural = "device types"


class DeviceModeOfOperation(models.Model):
    id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=255, default='prenosné', unique=True)

    def __str__(self):
        return str(self.operation)

    def __unicode__(self):
        return str(self.operation)

    class Meta:
        verbose_name_plural = "device modes"


class DeviceManufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "device manufacturers"


class DeviceCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "device categories"


class DeviceUseGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.CharField(max_length=255)

    def __str__(self):
        return str(self.group)

    def __unicode__(self):
        return str(self.group)

    class Meta:
        verbose_name_plural = "device groups"


class DeviceClass(models.Model):
    id = models.AutoField(primary_key=True)
    device_class = models.CharField(max_length=255)

    def __str__(self):
        return str(self.device_class)

    def __unicode__(self):
        return str(self.device_class)

    class Meta:
        verbose_name_plural = "device classes"


class DeviceModel(models.Model):
    # TYPE_CHOICES = (
    #     ('Spotrebič', 'Spotrebič'),
    #     ('Predlžovačka', 'Predlžovačka')
    # )

    # CLASS = (
    #     ('1', '1'),
    #     ('2', '2')
    # )

    # USE_GROUP = (
    #     ('A', 'A'),
    #     ('B', 'B'),
    #     ('C', 'C'),
    #     ('D', 'D'),
    #     ('E', 'E'),
    # )

    # OPERABILITY_CHOICES = (
    #     ('držané v ruke', 'držané v ruke'),
    #     ('prenosné', 'prenosné'),
    #     ('pripevnené, neprenosné','pripevnené, neprenosné')
    # )

    id = models.AutoField(primary_key=True)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    device_category = models.ForeignKey(DeviceCategory, on_delete=models.CASCADE)
    device_manufacturer = models.ForeignKey(DeviceManufacturer, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    device_class = models.ForeignKey(DeviceClass, on_delete=models.CASCADE)
    use_group = models.ForeignKey(DeviceUseGroup, on_delete=models.CASCADE)
    mode_of_operation = models.ForeignKey(DeviceModeOfOperation, on_delete=models.CASCADE, to_field='operation', default='prenosné')

    def __str__(self):
        return self.device_name

    def __unicode__(self):
        return self.device_name

    class Meta:
        verbose_name_plural = "device templates"
   

class Device(models.Model):
    # fields of the table
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    audit_no = models.IntegerField()
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    device_SN = models.CharField(max_length=255)
    cord = models.ForeignKey(Cord, on_delete=models.CASCADE)
    device_voltage = models.ForeignKey(Voltage, on_delete=models.CASCADE)
    power = models.DecimalField(max_digits=16, decimal_places=4)
    current = models.DecimalField(max_digits=16, decimal_places=4)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True, blank=True)
    qr_text = models.CharField(max_length=255)
    note = models.TextField(null=True, blank=True)

    # display names
    def __str__(self):
        return self.device_model.device_name

    def __unicode__(self):
        return self.device_model.device_name

    # display name of plural forms
    class Meta:
        verbose_name_plural = "devices"
