from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Distributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    # Add any additional fields specific to distributors
