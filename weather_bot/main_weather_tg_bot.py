import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import telebot
from telebot.types import BotCommand


bot = Bot(token=tg_bot_token)
bot1 = telebot.TeleBot(tg_bot_token, parse_mode="html")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    user = message.from_user
    await message.reply(f"Hi {user.first_name} tell me the name of the city and i will tell you the weather forecast!")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q=" + message.text + "&appid=" + open_weather_token + "&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look out the window, you don't understand what the weather is like!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Weather in the city: {city}\nTemperature: {cur_weather}C° {wd}\n"
                            f"Moisture: {humidity}%\nPressure: {pressure} mm.Hg\nThe wind is blowing: {wind} m/s\n"
                            f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nDuring the day: {length_of_the_day}\n"
                            f"***Have a good day!***"
                            )
    except:
        await message.reply("\U00002620 Check the city name \U00002620")


def my_commands():
    return [
        BotCommand("/start", "Start bot")
    ]


if __name__ == "__main__":
    print("Started...")
    bot1.set_my_commands(commands=my_commands())
    executor.start_polling(dp)


