import config
import telebot
from telebot import types
print(config.token)
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="1", callback_data="answ1")
    callback_button2 = types.InlineKeyboardButton(text="1", callback_data="answ1")
    callback_button3 = types.InlineKeyboardButton(text="1", callback_data="answ1")
    callback_button4 = types.InlineKeyboardButton(text="1", callback_data="answ1")
    keyboard.add(callback_button1)
    keyboard.add(callback_button2)
    keyboard.add(callback_button3)
    keyboard.add(callback_button4)
    bot.send_message(message.chat.id, "hello", reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()