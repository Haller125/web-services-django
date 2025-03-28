from django.db import models

# Create your models here.
class User(models.Model):
    CurrencyChoices = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
    ]

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    currency = models.CharField(choices=CurrencyChoices, max_length=3)
    balance = models.FloatField()
