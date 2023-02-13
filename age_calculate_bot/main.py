from datetime import datetime, date
import telebot
from telebot.types import BotCommand


API_TOKEN = "6251735390:AAEaPBuLaIkcrLSTZgL5kHA-GWH0HKAGaWY"
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    user = message.from_user
    answer = f"Assalomu alaykum {user.first_name}, Yoshingizni aniqlovchi botga xush kelibsiz!"
    bot.reply_to(message, answer)


@bot.message_handler(commands=['age'])
def get_age(message):
    msg = bot.reply_to(message, "Tug'ilgan yilingizni kiriting.")
    bot.register_next_step_handler(msg, get_age_func)


def get_age_func(message):
    current_year = int(datetime.now().strftime('%Y'))
    try:
        user_year = int(message.text)
    except Exception as e:
        answer = "Tug'ilgan yilingizni kiriting."
        bot.reply_to(message, answer)
    else:
        if user_year < current_year:
            text = f"Siz {current_year - user_year} yoshda siz."
            bot.reply_to(message, text)
        else:
            answer = "Iltimos tug'ilgan yilingizni to'g'ri kiriting!!"
            bot.reply_to(message, answer)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/age", "Age bot")
    ]


if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.polling()



