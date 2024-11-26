from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'salary_added']
