from django.db import models
from django.contrib.auth.models import AbstractUser

CurrencyChoices = [
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
]


# Create your models here.
class User(AbstractUser):
    currency = models.CharField(choices=CurrencyChoices, max_length=3, default='GBP')
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.username} - {self.currency} - {self.balance}"
