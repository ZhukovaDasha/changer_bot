import json
import requests
import telebot
from config import keys

class ConversionException(Exception):
    pass

class Change_Money:
    @staticmethod
    def convert( quote:str, base:str, amount:str):
        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}')
            bot.reply_to(message, f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Неудалось обработать валюту {quote}')
            bot.reply_to(message,f'Неудалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Неудалось обработать валюту {base}')
            bot.reply_to(message, f'Неудалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Неудалось обработать количество {amount}')
            bot.reply_to(message, f'Неудалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        total_base = json.loads(r.content)
        total_base = total_base[keys[base]]
        total_base = float(amount) * total_base

        return total_base
