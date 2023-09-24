from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from uuid import uuid4
from .models import Asset, MaintenanceReport
from .forms import MaintenanceReportForm



@login_required
def asset_list(request):
    # Fetch all assets from the database
    assets = Asset.objects.all()

    if request.method == 'POST':
        # Handle asset creation
        asset_name = request.POST.get('asset_name')
        asset_type = request.POST.get('asset_type')

        # Generate a unique URL (you can tailor this to your needs)
        unique_url = str(uuid4())

        # Create a new asset
        Asset.objects.create(
            asset_name=asset_name,
            asset_type=asset_type,
            unique_url=unique_url
        )
        return redirect('asset_list')

    return render(request, 'mod/asset_list.html', {'assets': assets})


@login_required
def update_asset(request):
    if request.method == 'POST':
        # Extract asset information from POST data
        asset_id = request.POST.get('id')
        asset_name = request.POST.get('asset_name')
        asset_type = request.POST.get('asset_type')
        
        # Fetch the asset by ID and update its fields
        asset = Asset.objects.get(id=asset_id)
        asset.asset_name = asset_name
        asset.asset_type = asset_type
        asset.save()
        
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

@login_required
def delete_asset(request):
    if request.method == 'DELETE':
        asset_id = request.GET.get('id')
        Asset.objects.filter(id=asset_id).delete()
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})

@login_required
def create_maintenance_report(request, asset_id=None):
    asset_readonly = False  # Default to not read-only
    initial_data = {'maintenance_start_time': timezone.now()}  # Auto-fill with current time
    
    if asset_id:
        asset = get_object_or_404(Asset, id=asset_id)
        asset_readonly = True  # Make read-only since asset_id is provided
        initial_data['asset'] = asset

    if request.method == 'POST':
        form = MaintenanceReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.maintenance_end_time = timezone.now()  # Auto-fill end time
            report.save()
            # Redirect or other actions...
    else:
        form = MaintenanceReportForm(initial=initial_data)
        
    if asset_readonly:
        form.fields['asset'].widget.attrs['readonly'] = True
        form.fields['asset'].disabled = True  # Ensure the value is not editable

    return render(request, 'mod/create_maintenance_report.html', {'form': form})

@login_required
def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    maintenance_reports = MaintenanceReport.objects.filter(asset=asset).order_by('-maintenance_start_time')
    
    context = {
        'asset': asset,
        'maintenance_reports': maintenance_reports,
    }
    
    return render(request, 'mod/asset_detail.html', context)