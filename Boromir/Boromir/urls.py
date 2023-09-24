from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assets.urls')),  # Include the URL patterns from your 'assets' app
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assets.urls')),  # Include the URL patterns from your 'assets' app
]
