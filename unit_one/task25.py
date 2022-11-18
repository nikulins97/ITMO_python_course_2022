#todo: Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.
#
# Input             	            Output
#
# apple	                        aple
# 25.04.2022 Good morning !!	    godmrni

alphabet='abcdefghijklmnopqrstuvwxyz'
new_text=input('Введите текст: ')
new_text=new_text.lower()

def coding():                                           # Функция записи алфавита
    global encoded_string
    encoded_string=''

    for i in new_text:
        if i in alphabet and i not in encoded_string:
            encoded_string+=i

    print('Получилось:',encoded_string)

coding()                                                #Вызов функции записи

