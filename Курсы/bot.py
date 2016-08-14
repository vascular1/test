# -*- coding: utf-8 -*-
import telepot
import requests


def chat(msg):
    chat_id= msg["chat"]["id"]
    text=msg["text"]
    #text=str(eval(text))
    if "/p24"==text:
        hr="https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
        r=requests.get(hr)
        data=r.json()
        s=''
        for i in data:
            s+="{}:{}/{}\n".format(i["ccy"],i["buy"],i["sale"])
        text=s
    else:
        
        lang="ru-en"
        msg= text
        key = "trnsl.1.1.20160725T230300Z.5c6a542dc27e3a7d.3baed373aed1a3a990ad18f8e652adea67d14f72"
        url_translate_yandex = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        r = requests.post(url_translate_yandex, data = {'key':key, 'text':msg, 'lang':lang})
        #https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160725T230300Z.5c6a542dc27e3a7d.3baed373aed1a3a990ad18f8e652adea67d14f72&text=привет&lang=ru-en
        data=r.json()
        text=data["text"][0]

    bot.sendMessage(chat_id,text)
    
token="269798794:AAFtoBra3WhesBcG6VMWrUONl3gb_llcseA"
bot=telepot.Bot(token)
print ("start")
bot.message_loop({"chat":chat},run_forever=True)
