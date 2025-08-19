from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username