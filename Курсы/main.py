# -*- coding: utf-8 -*-
#https://ide.c9.io/tolearn/ruby
import stemmer
stem = stemmer.Porter.stem
import numpy as np
LA = np.linalg
import pickle

titles =[
 	u"Британская полиция знает о местонахождении основателя WikiLeaks",
 	u"В суде США начинается процесс против россиянина, рассылавшего спам",
 	u"Церемонию вручения Нобелевской премии мира бойкотируют 19 стран",
 	u"В Великобритании арестован основатель сайта Wikileaks Джулиан Ассандж",
 	u"Украина игнорирует церемонию вручения Нобелевской премии",
 	u"Шведский суд отказался рассматривать апелляцию основателя Wikileaks",
 	u"НАТО и США разработали планы обороны стран Балтии против России",
 	u"Полиция Великобритании нашла основателя WikiLeaks, но, не арестовала",
 	u"В Стокгольме и Осло сегодня состоится вручение Нобелевских премий"
]

# Оставить только буквы и пробелы
new_titles = []
for title in titles:
    new_title = []
    for simbol in title:
        if simbol.isalpha():
            new_title.append(simbol)
        else:
            new_title.append(" ")
    new_titles.append(''.join(new_title))


for title in new_titles:
    print title
    
titles = new_titles
# Перевести в нижний регистр
new_titles = []
for title in titles:
    new_titles.append(title.lower())

print "\n\n" 
for title in new_titles:
    print title

titles = new_titles
# Разбить на слова
new_titles = []
for title in titles:
    new_titles.append(title.split())

print "\n\n" 
for title in new_titles:
    print ' '.join(title)

titles = new_titles
# Убрать слова длинной меньше 2-ух символов
new_titles = []
for title in titles:
    new_title = []
    for word in title:
        if len(word) > 2:
            new_title.append(word)
    new_titles.append(new_title)

print "\n\n" 
for title in new_titles:
    print ' '.join(title)
    
titles = new_titles
# Стемминг слов
new_titles = []
for title in titles:
    new_title = []
    for word in title:
        new_title.append(stem(word))
    new_titles.append(new_title)


print "\n\n" 
for title in new_titles:
    print ' '.join(title)

titles = new_titles
# Оставить слова, которые встречаются в разных строках
new_titles = []
for title in titles:
    new_titles.append(set(title))

titles = new_titles
new_titles = []
for title in titles:
    count_word = 0
    new_title = []
    for word in title:
        for title in titles:
            if word in title:
                count_word += 1
        if count_word > 1:
            new_title.append(word)
    new_titles.append(new_title)


print "\n\n" 
for title in new_titles:
    print ' '.join(title)
    
titles = new_titles
# Получить список всех слов
words = []
for title in titles:
    for word in title:
        words.append(word)
words = list(set(words))
print ' '.join(words)

# Создать матрицу
matrix = []
for word in words:
    row = []
    for title in titles:
        if word in title:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

print matrix

a = np.array(matrix)
U, s, Vh = LA.svd(a, full_matrices=False)


print "Vh =", Vh[:2]
titles = []
for row in Vh[:2]:
    titles.append(list(row))
titles = zip(titles[0], titles[1])

new_titles = []
my_title = titles[0]
for index, title in enumerate(titles[1:], start=2):
    distance = ((my_title[0]-title[0])**2+(my_title[1]-title[1])**2)**0.5
    new_titles.append([index, distance])
new_titles = sorted(new_titles, key=lambda x: x[1])
for title in new_titles:
    print title




matrix = []
for row in U:
    matrix.append(list(row[:2]))
#print matrix

with open('matrix.pickle', 'wb') as f:
    pickle.dump(matrix, f)
with open('words.pickle', 'wb') as f:
    pickle.dump(words, f)
with open('titles.pickle', 'wb') as f:
    pickle.dump(titles, f)
    