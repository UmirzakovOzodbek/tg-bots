import config as cfg
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


a = 0
keys = []
keyb = InlineKeyboardMarkup()
for i, j in cfg.LANGDICT.items():
    key = InlineKeyboardButton(j, callback_data=i)
    keys.append(key)
    a += 1
    if a == 3:
        a = 0
        keyb.add(keys[0], keys[1], keys[2])
        keys = []
