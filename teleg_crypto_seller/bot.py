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
        bot.send_message(call.message.chat.id, "Masz doświadczenie z inwestycjami?", reply_markup=keyboard)

    if call.data == "answ2":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="5000 $ miesięcznie", callback_data="answ3")
        callback_button2 = types.InlineKeyboardButton(text="10000 $ miesięcznie", callback_data="answ3")
        callback_button3 = types.InlineKeyboardButton(text="50000 $ miesięcznie", callback_data="answ3")
        callback_button4 = types.InlineKeyboardButton(text="100 000 $ lub więcej miesięcznie", callback_data="answ3")
        keyboard.add(callback_button1)
        keyboard.add(callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button4)
        bot.send_message(call.message.chat.id, "Jaki poziom dochodów jest Twoim ostatecznym celem?", reply_markup=keyboard)

    if call.data == "answ3":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Jestem osobą spontaniczną", callback_data="answ4")
        callback_button2 = types.InlineKeyboardButton(text="Gromadząc i analizując jak najwięcej informacji", callback_data="answ4")
        callback_button3 = types.InlineKeyboardButton(text="Konsultując się z ekspertami / profesjonalistami", callback_data="answ4")
        callback_button4 = types.InlineKeyboardButton(text="Konsultując się z rodziną lub przyjaciółmi", callback_data="answ4")
        keyboard.add(callback_button1)
        keyboard.add(callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button4)
        bot.send_message(call.message.chat.id, "Jak podchodzisz do podejmowania strategicznych decyzji?", reply_markup=keyboard)

    if call.data == "answ4":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Kryptowaluta", callback_data="answ5")
        callback_button2 = types.InlineKeyboardButton(text="Oszczędności", callback_data="answ5")
        callback_button3 = types.InlineKeyboardButton(text="Nieruchomość", callback_data="answ5")
        callback_button4 = types.InlineKeyboardButton(text="Złoto", callback_data="answ5")
        callback_button5 = types.InlineKeyboardButton(text="Dzieci", callback_data="answ5")
        keyboard.add(callback_button1)
        keyboard.add(callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button4)
        keyboard.add(callback_button5)
        bot.send_message(call.message.chat.id, "Sądząc z własnego doświadczenia, jak skuteczne były Twoje inwestycje w tych dziedzinach?", reply_markup=keyboard)

    if call.data == "answ5":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Kupiłbym drogi samochód", callback_data="answ6")
        callback_button2 = types.InlineKeyboardButton(text="Kupiłbym ładny dom", callback_data="answ6")
        callback_button3 = types.InlineKeyboardButton(text="Kupiłbym udziały w odnoszącej sukcesy firmie", callback_data="answ6")
        callback_button4 = types.InlineKeyboardButton(text="Spędziłbym to wszystko z przyjaciółmi", callback_data="answ6")
        callback_button5 = types.InlineKeyboardButton(text="Inwestowałbym na rynku walutowym", callback_data="answ6")
        keyboard.add(callback_button1)
        keyboard.add(callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button4)
        keyboard.add(callback_button5)
        bot.send_message(call.message.chat.id, "Gdybyś miał dużo pieniędzy, jak byś je wydał?", reply_markup=keyboard)

    if call.data == "answ6":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="250$", callback_data="answ7")
        callback_button2 = types.InlineKeyboardButton(text="1000$", callback_data="answ7")
        callback_button3 = types.InlineKeyboardButton(text="5000$", callback_data="answ7")
        callback_button4 = types.InlineKeyboardButton(text="10000$", callback_data="answ7")
        keyboard.add(callback_button1)
        keyboard.add(callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button4)
        bot.send_message(call.message.chat.id, "Ile masz kapitału na swoją początkową inwestycję?", reply_markup=keyboard)

    if call.data == "answ7":
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Twój wiek", url="https://dijaceqa.momonito.com/tracker?offer_id=3836&aff_id=9756")

        keyboard.add(url_button)

        bot.send_message(call.message.chat.id, "Proszę wprowadzić swój wiek. Aby wziąć udział, musisz mieć ukończone 18 lat", reply_markup=keyboard)

if __name__ == '__main__':
    bot.infinity_polling()