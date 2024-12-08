from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('send-notifications/', views.send_bulk_notifications, name='send_bulk_notifications'),
]
