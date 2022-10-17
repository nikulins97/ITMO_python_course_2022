#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#чтобы каждая функция выполняла одно универсальное действие.

import random
words = ['оператор','конструкция','объект']
desc=['Это слово обозначает наименьшую автономную часть языка программирования','Это слово означает construction','Это слово означает Object']
#Блок рандомайза слова
random_index=random.randint(0, len(words)-1)
secret=words[random_index] #загаданое_слово
print(desc[random_index])

letter=""

answer=["_" for x in words[random_index]]           #Поле задания ответа
lives=9 #кол-во жизней
def tablo():                                          #Функция вывода табло
    global letter
    if ("".join(answer))==secret and lives>0:
        print("".join(answer))
        print("\n","Поздравляю, вы выиграли!")
    elif lives==0:
        print('Игра окончена, вы проиграли! :(')
        print('Было загадано слово:',secret)
    else:
        print("".join(answer))
        letter=input('Введите следующую букву:')

def life(live):                                             #Функция контроля жизней
    global lives
    lives=lives-1
    print('Нет такой буквы. У вас осталось',lives,'жизней')

def game_algorythm(word,letter):                                  #Функция игрового алгоритма
    global answer
    #случай единичного вхождения
    if list(secret).count(letter) == 1:
        ind = list(secret).index(letter)
        answer[ind] = letter
    #случай множественного вхождения
    else:
        start = 0
        for n in range(list(secret).count(letter)):
            ind = list(secret).index(letter, start, len(secret))
            start = ind + 1
            answer[ind] = letter
#Тело игры
while ("".join(answer))!=secret:
    tablo()
    if letter not in secret:
        life(lives)
        if lives==0:
            break
    else:
        game_algorythm(secret,letter)
tablo()