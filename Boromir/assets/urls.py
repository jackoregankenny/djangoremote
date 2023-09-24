from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Admin URLs
    path('asset_list/', views.asset_list, name='asset_list'),
    path('mod/asset_detail/<int:asset_id>/', views.asset_detail, name='asset_detail'),

   
    
    path('mod/update_asset/', views.update_asset, name='update_asset'),
    path('mod/delete_asset/', views.delete_asset, name='delete_asset'),


    path('maint/', views.create_maintenance_report, name='maint_no_id'),
    path('maint/<int:asset_id>/', views.create_maintenance_report, name='maint_with_id'),


    # Add more admin-specific URLs here

    # User URLs 
    #path('user/dashboard/', views.user_dashboard, name='user_dashboard'),  # Example user page
    # Add more user-specific URLs here
]
