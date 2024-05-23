from django.db import models


# Create your models here.
class rideBook(models.Model):
    pick_loc = models.CharField(max_length=150)
    drop_loc = models.CharField(max_length=150)
    vehicle_class = models.CharField(max_length=9)
    vehicle_type = models.CharField(max_length=4)
    booked_by = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    car = models.CharField(max_length=10)
