from datetime import datetime, date
import telebot
from telebot.types import BotCommand


API_TOKEN = "6251735390:AAEaPBuLaIkcrLSTZgL5kHA-GWH0HKAGaWY"
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    user = message.from_user
    answer = f"Assalomu alaykum {user.first_name}, Xush kelibsiz!"
    answer += "\nTug'ulgan yilingizni kiriting:"
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda message: True)
def calculate_age(message):
    today = date.today()
    age = today.year - message - ((today.month, today.day) < (message.month, message.day))
    birth_date = date(message, 12, 12)
    bot.reply_to(birth_date, f"Yosh: {age}")


def my_commands():
    return [
        BotCommand("/start", "Start bot")
    ]


if __name__ == "__main__":
    bot.set_my_commands(commands=my_commands())
    bot.polling()



