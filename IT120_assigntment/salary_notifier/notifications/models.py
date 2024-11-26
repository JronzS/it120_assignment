from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    bank_account = models.CharField(max_length=50)
    salary_added = models.BooleanField(default=False)

    def __str__(self):
        return self.name
