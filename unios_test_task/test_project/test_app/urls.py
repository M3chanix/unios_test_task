from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/events', views.device_list, name='device_list')
]
