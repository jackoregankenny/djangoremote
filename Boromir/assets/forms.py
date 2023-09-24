from django import forms
from .models import Asset, MaintenanceReport

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

class MaintenanceReportForm(forms.ModelForm):
    maintenance_end_time = forms.DateTimeField(required=False, disabled=True)
    maintenance_checkout_time = forms.DateTimeField(required=False)
    report_description = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = MaintenanceReport
        fields = [
            'asset',
            'maintenance_start_time',
            'maintenance_end_time',
            'maintenance_checkout_time',
            'maintenance_classification',
            'anomalies_flagged',
            'report_description',
        ]
