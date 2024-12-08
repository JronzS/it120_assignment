from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)  # Format: +639XXXXXXXXX
    bank_account = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class SalaryNotification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")  # e.g., Sent, Failed

    def __str__(self):
        return f"Notification to {self.employee.name} on {self.date_sent}"
