from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

languages_btn = ReplyKeyboardMarkup(resize_keyboard=True)

LANGUAGES = {
    "UZ 🇺🇿": "uz",
    "RU 🇷🇺": "ru",
    "EN 🇬🇧": "en"
}

languages_btn.add(
    KeyboardButton(list(LANGUAGES.keys())[0]),
    KeyboardButton(list(LANGUAGES.keys())[1]),
    KeyboardButton(list(LANGUAGES.keys())[2])
)

languages_inline_btn = InlineKeyboardMarkup()

languages_inline_btn.add(
    InlineKeyboardButton(list(LANGUAGES.keys())[0], callback_data=f"language_{list(LANGUAGES.values())[0]}"),
    InlineKeyboardButton(list(LANGUAGES.keys())[1], callback_data=f"language_{list(LANGUAGES.values())[1]}"),
    InlineKeyboardButton(list(LANGUAGES.keys())[2], callback_data=f"language_{list(LANGUAGES.values())[2]}"),
)


def get_language_btn(action):
    languages_inline_btn = InlineKeyboardMarkup()
    languages_inline_btn.add(
        InlineKeyboardButton(
            list(LANGUAGES.keys())[0], callback_data=f"{action}_language_{list(LANGUAGES.values())[0]}"
        ),
        InlineKeyboardButton(
            list(LANGUAGES.keys())[1], callback_data=f"{action}_language_{list(LANGUAGES.values())[1]}"
        ),
        InlineKeyboardButton(
            list(LANGUAGES.keys())[2], callback_data=f"{action}_language_{list(LANGUAGES.values())[2]}"
        ),
    )
    return languages_inline_btn


confirm_btn = ReplyKeyboardMarkup(resize_keyboard=True)

CONSENT = {
    "YES ✅": "yes",
    "NO ❌": "no"
}

# languages_btn.add(
#     KeyboardButton(list(LANGUAGES.keys())[0]),
#     KeyboardButton(list(LANGUAGES.keys())[1]),
#     KeyboardButton(list(LANGUAGES.keys())[2])
# )
#
# languages_inline_btn = InlineKeyboardMarkup()
#
# languages_inline_btn.add(
#     InlineKeyboardButton(list(LANGUAGES.keys())[0], callback_data=f"language_{list(LANGUAGES.values())[0]}"),
#     InlineKeyboardButton(list(LANGUAGES.keys())[1], callback_data=f"language_{list(LANGUAGES.values())[1]}"),
#     InlineKeyboardButton(list(LANGUAGES.keys())[2], callback_data=f"language_{list(LANGUAGES.values())[2]}"),
# )


share_phone_btn = ReplyKeyboardMarkup(resize_keyboard=True)
share_phone_btn.add(KeyboardButton("Share phone", request_contact=True))
