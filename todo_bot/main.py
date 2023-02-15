from datetime import datetime

import telebot
from environs import Env
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove

from keybords import languages_inline_btn
from messages import messages
from task import Chat, Task
from utils import write_row_to_csv, get_fullname, get_language_code_by_chat_id


BOT_TOKEN = "6154362259:AAG7TwOYqdlqu3BW2JFrEEGc-Z1wIFhOMXw"

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Assalomu alaykum, {fullname}", reply_markup=languages_inline_btn)
    # bot.register_next_step_handler(message, set_language_handler)


# def set_language_handler(message):
#     chat = message.chat
#     new_chat = Chat(
#         chat.id,
#         get_fullname(chat.first_name, chat.last_name),
#         LANGUAGES.get(message.text)
#     )
#     write_row_to_csv(
#         "chats.csv",
#         list(new_chat.get_attrs_as_dict().keys()),
#         new_chat.get_attrs_as_dict()
#     )
#     bot.send_message(chat.id, messages[LANGUAGES.get(message.text)].get("add_task"),
#     reply_markup=ReplyKeyboardRemove())


@bot.callback_query_handler(lambda call: call.data.startswith("language_"))
def set_language_query_handler(call):
    message = call.message
    lang_code = call.data.split("_")[1]
    chat = message.chat
    new_chat = Chat(
        chat.id,
        get_fullname(chat.first_name, chat.last_name),
        lang_code
    )
    write_row_to_csv(
        "chats.csv",
        list(new_chat.get_attrs_as_dict().keys()),
        new_chat.get_attrs_as_dict()
    )
    bot.delete_message(chat.id, message.id)
    bot.send_message(chat.id, messages[lang_code].get("add_task"))


# /add
@bot.message_handler(commands=["add"])
def add_task_handler(message):
    chat_id = message.chat.id
    lang_code = get_language_code_by_chat_id(chat_id, "chats.csv")
    msg = messages[lang_code].get("send_task")
    bot.send_message(message.chat.id, msg)

    bot.register_next_step_handler(message, get_task_handler)


@bot.message_handler(content_types=["text"])
def get_task_handler(message):
    chat_id = message.chat.id
    if message.content_type != "text":
        bot.send_message(chat_id, "Invalid format.")

    new_task = Task(chat_id, message.text, datetime.now())
    write_row_to_csv(
        "tasks.csv",
        list(new_task.get_attrs_as_dict().keys()),
        new_task.get_attrs_as_dict()
    )

    bot.send_message(chat_id, "Add successfully.")


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/add", "Add new task")
    ]


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
