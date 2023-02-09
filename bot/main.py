import json
from datetime import datetime
import telebot
from environs import Env
from student import Student
from utils import write_to_csv, is_exist_chat_id
from api.weather import WeatherManager


env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    # print(json.loads(message))
    chat_id = message.chat.id
    user = message.from_user
    fullname = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    bot.send_message(chat_id, f"Assalomu alaykum, {fullname}")
    if not is_exist_chat_id(chat_id):
        student = Student(chat_id, fullname)
        write_to_csv(student)
    else:
        print("User already exist.")


@bot.message_handler(commands=["weather"])
def weather_handler(message):
    today = datetime.now()
    weather_data = WeatherManager("tashkent").get_daily_temperature()
    today_weather = None
    for day_weather in weather_data:
        day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
        if day_date.date() == today.date():
            today_weather = day_weather
    msg = f"<b>Bugungi ob-havo:</b>\n\n" \
          f"<i>Harorat:</i> {today_weather.get('average_temperature')}"
    bot.send_message(message.chat.id, msg)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


def my_commands():



if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands()
    bot.infinity_polling()
