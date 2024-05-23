from django.contrib import admin
from .models import rideBook


# Register your models here.
class bookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pick_loc",
        "drop_loc",
        "vehicle_class",
        "vehicle_type",
        "booked_by",
        "time",
        "car",
    )


admin.site.register(rideBook, bookingAdmin)
