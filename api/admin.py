# Register your models here.
from django.contrib import admin
from api import models



class DeviceConfigAdmin(admin.ModelAdmin):
    list_display = [i.name for i in models.DeviceConfig._meta.fields]
    list_display_links = list_display


class DeviceStatusAdmin(admin.ModelAdmin):
    list_display = [i.name for i in models.DeviceStatus._meta.fields]
    list_display_links = list_display


admin.site.register(models.DeviceConfig, DeviceConfigAdmin)

admin.site.register(models.DeviceStatus, DeviceStatusAdmin)
