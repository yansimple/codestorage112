
import telebot
from clarifai.rest import ClarifaiApp
from telebot import types

tgToken = "714178838:AAHyQ0jDs_pKQO1dRNOglijjnEPs19grFPE"

app = ClarifaiApp(api_key='6560ad9e6b72492a9a3855faa7c307a9')
model = app.public_models.general_model

bot = telebot.TeleBot(tgToken)

@bot.message_handler(command=['start'])

def start(massage):
    info_text = "Это бот от @yansimple Отправьте ему изображение"
    print("| User ID: ", massage.chat.id, " start")
    bot.send_message(massage.chat.id, info_text)

@bot.message_handler(content_types=["text"])
def take_user(massage):
    link = massage.text
    response = model.predict_by_url(url=link)
    string = ""
    for i in response["outputs"][0]['data']["concepts"]:
        txt=str(i['name']+"\n")
        print(txt)
        string = string + txt
    STR = string +"\n"+link
    bot.send_message(massage.chat.id, STR)       
    

if __name__ == '__main__':
    bot.polling(none_stop=True)
