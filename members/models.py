from django.db import models


# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=60)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    level = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
