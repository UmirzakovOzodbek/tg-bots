from transliterate import to_latin, to_cyrillic
import telebot


API_TOKEN = "6077440048:AAEsz5W8EuPog3Sn23BlOHJrVyJJuG8w7Bs"
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    user = message.from_user
    answer = f"Assalomu alaykum {user.first_name}, Xush kelibsiz!"
    answer += "\nMatn kiriting:"
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer(msg))


if __name__ == "__main__":
    bot.polling()






