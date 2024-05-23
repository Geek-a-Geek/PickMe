from django.db import models


# Create your models here.
class service(models.Model):
    service_type = models.CharField(max_length=8)
    vehicle_type = models.CharField(max_length=4)
    description = models.CharField(max_length=150)
    charge = models.IntegerField()
