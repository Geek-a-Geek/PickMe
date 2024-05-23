from django.db import models


# Create your models here.
class vehicles(models.Model):
    reg_num = models.CharField(max_length=10)
    chassis_num = models.CharField(max_length=17)
    engine_num = models.CharField(max_length=19)
    vehicle_class = models.CharField(max_length=9)
    vehicle_type = models.CharField(max_length=4)
    available = models.BooleanField(default=True)
