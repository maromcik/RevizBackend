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
    path('get_devices/', views.get_devices, name='get_devices'),
    path('get_models/', views.get_models, name='get_models'),
    path('get_facilities/', views.get_facilities, name='get_facilities'),
    path('get_facility_by_name/<str:facility_name>/', views.get_facility_by_name, name='get_facilities_by_name'),
    path('<str:qr>/get/', views.get_device, name='get_device'),
    path('<str:qr>/update/', views.update_device, name='update_device'),
    path('<str:qr>/delete/', views.delete_device, name='delete_device'),
    path('create_device/', views.create_device, name='create_device'),
    path('get_devices_by_facility/<str:facility_name>/', views.get_devices_by_facility, name='get_devices_by_facility'),
]