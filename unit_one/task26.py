#todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 classwork/task3
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
#
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
#
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.

import random
import pickle

data=[]

guess=str(random.randint(0,100))
lives=5


def menu():
    out = f"1. Новая игра\n2. Продолжить\n3. Сохранить игру\n4. Загрузить игру"
    print(out)

def save_game():
    name=input('Введите название игры:')
    data=get_save_game()
    save_point={"name":name, "guess":guess, "lives":lives}
    data.append(save_point)
    with open('game_dump.pkl','wb') as f:
        pickle.dump(data,f)

def get_save_game():
    with open('game_dump.pkl', 'r') as f:
        data=pickle.load(f)
        return data

def open_game():
    with open('game_dump.pkl', 'wb') as f:
        data=pickle.load(f)
        count=1
        for dict in data:
            str=f"{count}:{dict['name']}"
            count+=1
            print(str)

        name_save_game = input("Введите имя")
        global guess, lives
        for dict in data:
            if name_save_game == dict["name"]:
                magic_num = dict["magic_num"]
                lives = dict["lives"]
                print(f"Игра восстановлена {dict['name']}")


def game():
    menu()
    num = int(input('Введите пункт меню: '))
    global lives
    if num == 4:
        open_game()
        num = 1

    if num == 1:
        # Начало игры

        while lives > 0:
            a = input('\n''Введите число от 0 до 100:')
            if a == guess:
                print('Вы угадали! Было загадано число:', guess)
            elif a=='s':
                save_game()
            else:
                lives -= 1
                print('\n''Неверно! У вас осталось {0} попыток'.format(lives))
                if lives == 0:
                    print('\n''Вы проиграли! Загадано число: ', guess)


game()

