from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee, SalaryNotification

# Register the Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'bank_account', 'salary')  # Columns to display in the list view
    search_fields = ('name', 'phone_number', 'bank_account')  # Fields to search in the admin panel

# Register the SalaryNotification model
@admin.register(SalaryNotification)
class SalaryNotificationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'status', 'date_sent')  # Columns to display in the list view
    list_filter = ('status', 'date_sent')  # Filters to filter records by status and date_sent
    search_fields = ('employee__name', 'status')  # Fields to search in the admin panel
