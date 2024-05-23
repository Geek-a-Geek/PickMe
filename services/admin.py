from django.contrib import admin
from .models import service


# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    list_display = ("service_type", "vehicle_type", "description", "charge")


admin.site.register(service, serviceAdmin)
