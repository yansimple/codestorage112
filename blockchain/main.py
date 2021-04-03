# -*- coding: utf-8 -*-
import json
import telebot

token = "880113181:AAH7gjTlSprxkVjavHT-lvHb5tnwV1ioLO8"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def tx_notif(massage):
    wallet = massage.text
    url = 'https://blockchain.info/rawaddr/' + wallet
    response = urlopen(url)
    url1 = "https://blockchain.info/q/getblockcount"
    response1 = urlopen(url1)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    string1 = response1.read().decode('utf-8')
    all_blocks = json.loads(string1)
    tx_id = json_obj['txs'][0]['inputs'][0]["prev_out"]['spending_outpoints'][0]['tx_index']
    link_tx = "https://blockchain.info/rawtx/" + str(tx_id)
    response_tr = urlopen(link_tx)
    string_tr = response_tr.read().decode('utf-8')
    height_json = json.loads(string_tr)
    mes1 = "Адрес '" + str(wallet) + "' получен успешно, последняя транзакция отслежена, ID транзакции - " + str(
        tx_id) + "\nОжидайте уведомления!"
    bot.send_message(massage.chat.id, mes1)
    while True:
        try:
            height = height_json["block_height"]
            number_conf = all_blocks - height + 1
            print(number_conf)
            if number_conf >= 2:
                print("NOTIFICATION! ", massage.chat.id)
                mes_notif = "Получено " + str(number_conf) + " подтверждения на транзакции " + str(
                    tx_id) + " Ваш кошелек '" + str(wallet) + "'\nЕсть вопросы? Напишите @yansimple"
                bot.send_message(massage.chat.id, mes_notif)
                break
        except:
            sleep(10)
            print("sleeping now 10 sec")
            continue


if __name__ == '__main__':
    bot.polling(none_stop=True)