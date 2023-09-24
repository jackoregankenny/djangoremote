from django.db import models

# Assets Table
class Asset(models.Model):
    asset_name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    asset_status = models.CharField(max_length=255)
    unique_url = models.URLField(unique=True)
    permissions_required = models.BooleanField(default=False)

# Maintenance Reports Table
class MaintenanceReport(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    maintenance_start_time = models.DateTimeField()
    maintenance_end_time = models.DateTimeField()
    maintenance_checkout_time = models.DateTimeField()
    maintenance_classification = models.CharField(max_length=255)
    anomalies_flagged = models.BooleanField(default=False)
    report_description = models.TextField(null=True, blank=True)


# Parts Table
class Part(models.Model):
    part_name = models.CharField(max_length=255)
    part_type = models.CharField(max_length=255)
    inventory_count = models.IntegerField()

# Linking Parts to Maintenance Reports in a Many-to-Many relationship
MaintenanceReport.parts_used = models.ManyToManyField(Part)

# Faults Table
class Fault(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    maintenance_report = models.ForeignKey(MaintenanceReport, on_delete=models.CASCADE, null=True, blank=True)
    severity = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])