from telebot.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)


def get_languages_btn(action):
    languages = {
        "UZ 🇺🇿": "uz",
        "RU 🇷🇺": "ru",
        "ENG 🇬🇧": "en"
    }

    languages_inline_btn = InlineKeyboardMarkup()

    languages_inline_btn.add(
        InlineKeyboardButton(
            list(languages.keys())[0], callback_data=f"{action}_language_{list(languages.values())[0]}"
        ),
        InlineKeyboardButton(
            list(languages.keys())[1], callback_data=f"{action}_language_{list(languages.values())[1]}"
        ),
        InlineKeyboardButton(
            list(languages.keys())[2], callback_data=f"{action}_language_{list(languages.values())[2]}"
        )
    )
    return languages_inline_btn


def storage_inline_btn(action):
    storage = {
        "✅": "OK",
        "❌": "NO"
    }
    storage_btn = InlineKeyboardMarkup()
    storage_btn.add(
        InlineKeyboardButton(list(storage.keys())[0], callback_data=f"{action}_{list(storage.values())[0]}"),
        InlineKeyboardButton(list(storage.keys())[1], callback_data=f"{action}_{list(storage.values())[1]}")
    )
    return storage_btn


share_phone_btn = ReplyKeyboardMarkup(resize_keyboard=True)
share_phone_btn.add(KeyboardButton("Share phone", request_contact=True))
