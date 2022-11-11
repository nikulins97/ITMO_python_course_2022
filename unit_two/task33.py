# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:
#  1. пользователь ввел некорректное значение в заданном диапазоне
#  2. результат запроса вернул 0 строк
#  3. Произошел разрыв соединения с сервером

#1

a=int(input('Введите число от 1 до 10: '))
class CorrectValue(Exception):
    def __init__(self):
        super().__init__()

try:
    if a>10 or a<0:
        raise CorrectValue
except CorrectValue as e:
    print(e,'Число должно быть в диапазоне от 1 до 10')
else:
    print('Введённое число входит в диапазон -',a)
finally:
    print('Выполнение программы завершено')


#2

import psycopg2
conn=psycopg2.connect(host='localhost', database='task',user='postgres', password='3321')

cur=connect.cursor()
class EmptyString(Exception):
    def __init__(self):
        super().__init__()

try:
    SQL_LINE=f"""SELECT name from task where id=8"""
    cur.execute(SQL_LINE)

    records=cur.fetchall()
    if not records:
        raise EmptyString()

except EmtiString as e:
    print(e,'Пользователь с данным id не найден')

else:
    for row in records:
        print(row)

finally:
    print('Выполнение программы завершено')


#3

import psycopg2

class ConnectionError(Exception):

    def __init__(self):
        super().__init__()

try:
    conn=psycopg2.connect(host='localhost', database='task',user='postgres', password='3321')
    raise ConnectionError()
except ConnectionError as e:
    print(e,'Произошёл разрыв соединения с сервером')
else:
    print(conn,'Соединение успешно установлено')
finally:
    print('Выполнение программы завершено')

