from django.contrib import admin
from .models import vehicles


# Register your models here.
class vehiclesAdmin(admin.ModelAdmin):
    list_display = (
        "reg_num",
        "chassis_num",
        "engine_num",
        "vehicle_class",
        "vehicle_type",
        "available",
    )


admin.site.register(vehicles, vehiclesAdmin)
