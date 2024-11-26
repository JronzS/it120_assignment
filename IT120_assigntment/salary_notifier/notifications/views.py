from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Employee
from .utils import send_sms

def notify_employees(request):
    employees = Employee.objects.filter(salary_added=False)

    for employee in employees:
        message = f"Hi {employee.name}, your salary has been credited to your account: {employee.bank_account}."
        if send_sms(employee.phone_number, message):
            employee.salary_added = True
            employee.save()

    return JsonResponse({"status": "Notifications sent"})
