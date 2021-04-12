import config
import telebot
from telebot import types
print(config.token)
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Chcę nauczyć się handlować", callback_data="answ1")
    callback_button2 = types.InlineKeyboardButton(text="Chcę zacząć zarabiać", callback_data="answ1")
    callback_button3 = types.InlineKeyboardButton(text="Uważam handel Bitcoinami za hobby", callback_data="answ1")
    callback_button4 = types.InlineKeyboardButton(text="Do celów inwestycyjnych", callback_data="answ1")
    keyboard.add(callback_button1)
    keyboard.add(callback_button2)
    keyboard.add(callback_button3)
    keyboard.add(callback_button4)
    bot.send_message(message.chat.id, "Dlaczego interesujesz się Bitcoinem?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "answ1":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Tak, udany", callback_data="answ2")
        callback_button2 = types.InlineKeyboardButton(text="Nie", callback_data="answ2")
        callback_button3 = types.InlineKeyboardButton(text="Tak, ale niezbyt dobry", callback_data="answ2")
        keyboard.add(callback_button1)
        keyboard.add(callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button4)
        bot.send_message(call.message.chat.id, "Masz doświadczenie z inwestycjami?", reply_markup=keyboard)

    if call.data == "answ2":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="5000 $ miesięcznie", callback_data="answ3")
        callback_button2 = types.InlineKeyboardButton(text="10000 $ miesięcznie", callback_data="answ3")
        callback_button3 = types.InlineKeyboardButton(text="50000 $ miesięcznie", callback_data="answ3")
        callback_button2 = types.InlineKeyboardButton(text="100 000 $ lub więcej miesięcznie", callback_data="answ3")
        keyboard.add(callback_button1)
        keyboard.add(callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button4)
        bot.send_message(call.message.chat.id, "Jaki poziom dochodów jest Twoim ostatecznym celem?", reply_markup=keyboard)



if __name__ == '__main__':
    bot.infinity_polling()