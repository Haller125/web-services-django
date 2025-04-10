from django.db import models
from django.contrib.auth.models import AbstractUser

CurrencyChoices = [
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
]


# Create your models here.
class User(AbstractUser):
    currency = models.CharField(choices=CurrencyChoices, max_length=3)
    balance = models.FloatField(default=0.0)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} - {self.email}"
