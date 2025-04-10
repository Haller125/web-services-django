from django.db import models
from register.models import CurrencyChoices

TRANSACTION_TYPE = [
    ('PAYMENT', 'PAYMENT'),
    ('REQUEST', 'REQUEST'),
]

STATUS = [
    ('PENDING', 'PENDING'),
    ('COMPLETED', 'COMPLETED'),
    ('CANCELLED', 'CANCELLED'),
]

# Create your models here.
class Transaction(models.Model):

    sender = models.ForeignKey('register.User', on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey('register.User', on_delete=models.CASCADE, related_name='recipient')
    amount = models.FloatField()
    currency = models.CharField(max_length=3, choices=CurrencyChoices)
    timestamp = models.CharField(max_length=50)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=16)
    status = models.CharField(choices=STATUS, max_length=10)
