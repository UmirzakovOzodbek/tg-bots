import json
import requests
from config import tg_bot_token
import telebot
from telebot.types import BotCommand


bot = telebot.TeleBot(tg_bot_token, parse_mode=None)


@bot.message_handler(commands=["start"])
def start_command(message):
    user = message.from_user
    answer = f"Assalomu alaykum {user.first_name}, Xush kelibsiz!"
    bot.reply_to(message, answer)


@bot.message_handler(commands=['currency'])
def get_age(message):
    answer = "Valyutani kiriting(UZB):"
    msg = bot.reply_to(message, answer)
    bot.register_next_step_handler(msg, convert)


currency = ["UZS"]


def convert(message):
    import requests

    currency_1 = message
    currency_2 = message
    amount = 10

    url = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    headers = {
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com",
        "x-rapidapi-key": "91d8898136msh83f56071c8737b2p1cbab2jsn4413d1661d85"
    }
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)

    for i in data:
        if i['Ccy'] == currency_1 and currency_2 == "UZS":
            float_value = float(i["Rate"])
            amount = float(amount)
            return float_value * amount
        elif i['Ccy'] == currency_2 and currency_1 == "UZS":
            float_value = float(i["Rate"])
            amount = float(amount)
            return amount / float_value
        elif currency_1 == i['Ccy']:
            for r in data:
                if currency_2 == r['Ccy']:
                    first_value = float(i["Rate"])
                    second_value = float(r["Rate"])
                    return first_value / second_value
        else:
            if currency_1 == "UZS" and currency_2 == "UZS":
                return float(amount)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/currency", "Currency convert bot")
    ]


if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.polling()
