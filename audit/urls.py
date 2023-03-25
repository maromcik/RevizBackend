"""Reviz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include

urlpatterns = [
    path('get_cities/', views.get_cities, name='get_cities'),
    path('get_locations/', views.get_locations, name='get_locations'),
    path('get_companies/', views.get_companies, name='get_companies'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('get_rooms/', views.get_rooms, name='get_rooms'),
    path('get_years/', views.get_year, name='get_year'),
    path('get_cords/', views.get_cords, name='get_cords'),
    path('get_voltages/', views.get_voltages, name='get_voltages'),
    path('get_device_types/', views.get_device_types, name='get_device_types'),
    path('get_device_mode_operations/', views.get_device_mode_operations, name='get_device_mode_operations'),
    path('get_device_manufacturers/', views.get_device_manufacturers, name='get_device_manufacturers'),
    path('get_device_categories/', views.get_device_categories, name='get_device_categories'),
    path('get_device_use_groups/', views.get_device_use_groups, name='get_device_use_groups'),
    path('get_device_classes/', views.get_device_classes, name='get_device_classes'),
    path('get_models/', views.get_models, name='get_models'),
    path('get_devices/', views.get_devices, name='get_devices'),
    path('push_cords/', views.push_cords, name='push_cords'),
    path('push_devices/', views.push_devices, name='push_devices'),
    path('push_device_manufacturers/', views.push_device_manufacturers, name='push_device_manufacturers'),
    path('push_models/', views.push_device_models, name='push_models'),
    path('push_rooms/', views.push_rooms, name='push_rooms'),
    path('push_voltages/', views.push_voltages, name='push_voltages'),
    path('push_years/', views.push_years, name='push_years'),

    # path('get_facility_by_name/<str:facility_name>/', views.get_facility_by_name, name='get_facilities_by_name'),
    # path('<str:qr>/get/', views.get_device, name='get_device'),
    # path('<str:qr>/update/', views.update_device, name='update_device'),
    # path('<str:qr>/delete/', views.delete_device, name='delete_device'),
    # path('create_device/', views.create_device, name='create_device'),
    # path('get_devices_by_facility/<str:facility_name>/', views.get_devices_by_facility, name='get_devices_by_facility'),
]
