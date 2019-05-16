import uuid

from django.db import models
from django.urls import reverse


class Address(models.Model):
    street = models.CharField(max_length=200)

    def __str__(self):
        return self.street


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this device.")
    serial_number = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} ({1})'.format(self.address, self.serial_number)

    def get_absolute_url(self):
        return reverse('device-details', args=[str(self.id)])
