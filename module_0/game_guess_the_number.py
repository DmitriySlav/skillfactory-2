#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

count = 0                           # счетчик попыток
number = np.random.randint(1,101)   # загадали число
print ("Загадано число от 1 до 100. У Вас есть 7 попыток") # даём только 7 попыток, этого вполне достаточно, 
                                                           # если играть по технологии "дели диапазон на двое"
attempts = 0                        # счетчик попыток угадывания

while attempts < 7:                        # бесконечный цикл
    predict = int(input())         # предполагаемое число
    count += 1                     # плюсуем попытку
    attempts += 1 
    if number == predict: 
        print (f"Поздравляю! Вы угадали число {number} за {count} попыток."); break   # число угадано, выходим из цикла
    elif number > predict: 
        print (f"Угадываемое число больше {predict} ")
        print (f"У Вас осталось {7 - attempts} попыток")
    elif number < predict: 
        print (f"Угадываемое число меньше {predict} ")
        print (f"У Вас осталось {7 - attempts} попыток")
if attempts == 7:
    print ("Вы проиграли!")     

