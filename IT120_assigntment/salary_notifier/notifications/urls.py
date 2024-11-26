from django.urls import path
from .views import notify_employees

urlpatterns = [
    path('notify-employees/', notify_employees, name='notify_employees'),
]
