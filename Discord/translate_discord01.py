#coding=utf-8
import discord
import requests
from langdetect import *
DetectorFactory.seed = 0
token = "trnsl.1.1.20181225T164207Z.d387221d99499e03.6560c4f87dcde022b22f89b71e36db58d709bac8"
token_discord ='NTUwNjk3OTk4NTU2ODU2MzMw.D1pwrg.GVnAGTwneWfj_guSjJkvsuR3Xxs'
client = discord.Client()
@client.event
async def on_ready():
    print("\nSTART WORKING\n")
@client.event
async def on_message(message):
    input_user = message.content
    eng_text = input_user
    print(message.author,"\n")
    if message.author.name != "Translate_YanSimple":
        List_langs = detect(eng_text)
        if List_langs == "en" or "so":
            url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
            trans_option = {'key':token, 'lang':'en-ru', 'text': eng_text}
            webRequest = requests.get(url_trans, params = trans_option)
            rus_text = webRequest.text
            rus_text = rus_text[36:(len(rus_text)-3)]
            print(eng_text," --- ", rus_text, "\n", message.author.name)
            rus_text = message.author.name + "\n" + rus_text + "\npre-alfa version"
            await message.channel.send(rus_text)
            print(List_langs)

        if List_langs == "ru" or "mk":
            url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
            trans_option = {'key':token, 'lang':'ru-en', 'text': eng_text}
            webRequest = requests.get(url_trans, params = trans_option)
            rus_text = webRequest.text
            rus_text = rus_text[36:(len(rus_text)-3)]
            print(eng_text," --- ", rus_text, "\n", message.author.name)
            rus_text = message.author.name + "\n" + rus_text + "\npre-alfa version"
            await message.channel.send(rus_text)
            print(List_langs)


client.run(token_discord)
