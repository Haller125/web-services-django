def convert_from_gbp(currency_from, currency_to, amount):
    change_rate_from_GBP = {
        'USD': 1.29,
        'EUR': 1.20,
        'GBP': 1.00,
    }

    return amount / change_rate_from_GBP[currency_from] * change_rate_from_GBP[currency_to]
