from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CurrencyConversionView(APIView):
    def get(self, request, currency1, currency2, amount):
        amount = float(amount)
        try:
            converted_amount = self.convert(currency1.upper(), currency2.upper(), amount)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "from": currency1.upper(),
            "to": currency2.upper(),
            "amount": amount,
            "converted": round(converted_amount, 2)
        })

    def convert(self, currency_from, currency_to, amount):
        change_rate_from_GBP = {
            'USD': 1.29,
            'EUR': 1.20,
            'GBP': 1.00,
        }

        if currency_from not in change_rate_from_GBP or currency_to not in change_rate_from_GBP:
            raise ValueError("Invalid currency")

        return amount / change_rate_from_GBP[currency_from] * change_rate_from_GBP[currency_to]
