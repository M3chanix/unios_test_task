from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/events', views.state_list, name='state_list'),
    path('api/delete/<int:pk>/', views.delete, name='delete'),
    path('api/edit/<int:pk>/', views.edit, name='edit'),
    path('api/save/<int:pk>/', views.save, name='save'),
    path('api/auth', views.auth, name='auth'),
    path('api/login', views.login, name='login')
]
