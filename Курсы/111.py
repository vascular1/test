# -*- coding: utf-8 -*-
import stemmer
stem=stemmer.Porter.stem
titles =[
 	u"Британская полиция знает о местонахождении основателя WikiLeaks",
 	u"В суде США начинается процесс против россиянина, рассылавшего спам",
 	u"Церемонию вручения Нобелевской премии мира бойкотируют 19 стран",
 	u"В Великобритании арестован основатель сайта Wikileaks Джулиан Ассандж",
 	u"Украина игнорирует церемонию вручения Нобелевской премии",
 	u"Шведский суд отказался рассматривать апелляцию основателя Wikileaks",
 	u"НАТО и США разработали планы обороны стран Балтии против России",
 	u"Полиция Великобритании нашла основателя WikiLeaks, но, не арестовала",
 	u"В Стокгольме и Осло сегодня состоится вручение Нобелевских премий xy"
]

new_titles=[]
for title in titles:
   # print title
    new_row=""
    for symbol in title:
        #print symbol
        if symbol.isalpha():
            new_row+=symbol
            
        else:
            new_row+=" "
    new_titles.append(new_row)

titles=new_titles
new_titles=[]
for title in titles:
    print title.lower()
    new_titles.append(title.lower())
titles=new_titles    
new_titles=[]
for title in titles:
    new_titles.append(title.split())

titles=new_titles
for title in titles:
    print " ".join(title)
    
new_titles=[]
for title in titles:
    new_title=[]
    for word in title:
       
        if len(word)>2:
    
            new_title.append(word)
    new_titles.append(new_title)
    print " ".join(new_title)
    
titles=new_titles    
new_titles=[]
for title in titles:
    new_title=[]
    for word in title:
        new_title.append(stem(word))
    new_titles.append(new_title)
    print " ".join(new_title)