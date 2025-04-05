from django.urls import path
from .views import CurrencyConversionView

urlpatterns = [
    path('<str:currency1>/<str:currency2>/<str:amount>/', CurrencyConversionView.as_view(), name='currency_conversion'),
]
