from types import MappingProxyType
from django.db import models

# Create your models here.
class laundry_location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name