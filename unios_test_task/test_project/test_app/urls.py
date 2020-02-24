from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/events', views.state_list, name='state_list'),
    path('api/delete/<int:pk>/', views.delete, name='delete'),
    path('api/change/<int:pk>/', views.change, name='change')
]
