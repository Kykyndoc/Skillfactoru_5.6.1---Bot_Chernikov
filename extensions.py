import requests
import json

keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}

class ConvertionException(Exception):
    pass

class PriceConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:   
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        quote_ticker, base_ticker = keys[quote], keys[base]
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?tsyms={base_ticker}&fsym={quote_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base *= int(amount)

        return total_base
