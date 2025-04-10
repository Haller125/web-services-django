from django import forms

class PaymentForm(forms.Form):
    recipient_email = forms.EmailField()
    amount = forms.FloatField(min_value=0.01)

class RequestForm(forms.Form):
    recipient_email = forms.EmailField()
    amount = forms.FloatField(min_value=0.01)
