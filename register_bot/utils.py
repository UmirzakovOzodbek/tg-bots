import csv
import os

from api.weather import WeatherManager


def write_to_csv(file_path, header, row):
    with open(file_path, "a", newline="\n", encoding="utf8") as file:
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize(file_path) == 0:
            csv_writer.writeheader()
        csv_writer.writerow(row)
    print("Student add successfully.")


def get_language_code_by_chat_id(chat_id, file_path):
    with open(file_path, encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        language = [
            row.get("language_code")
            for row in csv_reader
            if int(row.get("id")) == chat_id
        ]
        if language:
            return language[-1]
        else:
            return "uz"


def is_exist_chat_id(chat_id):
    with open("students.csv") as f:
        csv_reader = csv.DictReader(f)
        return chat_id in [int(row.get("chat_id")) for row in csv_reader]


def get_fullname(first_name, last_name):
    return f"{first_name} {last_name}" if last_name else first_name


def get_weather_days():
    temperatures = WeatherManager().get_daily_temperature()
    return [day_temp.get("day") for day_temp in temperatures]
