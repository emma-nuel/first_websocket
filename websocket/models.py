from django.db import models

# Create your models here.
class LocationData(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
