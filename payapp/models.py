from django.db import models

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('PAYMENT_SENT', 'PAYMENT_SENT'),
        ('PAYMENT_RECEIVED', 'PAYMENT_RECEIVED'),
        ('REQUEST_SENT', 'REQUEST_SENT'),
        ('REQUEST_RECEIVED', 'REQUEST_RECEIVED'),
    ]

    STATUS = [
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED'),
        ('CANCELLED', 'CANCELLED'),
    ]

    Sender = models.ForeignKey('register.User', on_delete=models.CASCADE, related_name='sender')
    Recipient = models.ForeignKey('register.User', on_delete=models.CASCADE, related_name='recipient')
    Amount = models.FloatField()
    Currency = models.CharField(max_length=3)
    Timestamp = models.DateTimeField(auto_now_add=True)
    TransactionType = models.CharField(choices=TRANSACTION_TYPE, max_length=16)
    Status = models.CharField(choices=STATUS, max_length=10)
