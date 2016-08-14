# -*- coding: utf-8 -*-
import requests
#r=requests.get(hr)
#data=r.json()
lang="ru-en"
msg= u"привет"

key = "trnsl.1.1.20160725T230300Z.5c6a542dc27e3a7d.3baed373aed1a3a990ad18f8e652adea67d14f72"
url_translate_yandex = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
r = requests.post(url_translate_yandex, data = {'key':key, 'text':msg, 'lang':lang})
#https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160725T230300Z.5c6a542dc27e3a7d.3baed373aed1a3a990ad18f8e652adea67d14f72&text=привет&lang=ru-en
data=r.json()
print data["text"][0]

  