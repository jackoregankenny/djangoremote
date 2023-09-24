from django.contrib import admin
from .models import Asset, MaintenanceReport, Part, Fault

# Register your models here.
admin.site.register(Asset)
admin.site.register(MaintenanceReport)
admin.site.register(Part)
admin.site.register(Fault)