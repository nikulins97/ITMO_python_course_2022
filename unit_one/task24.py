#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!



alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet_list=list(letter for letter in alphabet)
num_range=list(range(1,27))
numbers_list=[]
for n in num_range:
    numbers_list.append(str(n))


phrase=input('Введите фразу без пробелов:')                  # Ввод фразы для перевода в числа

def lett_to_numbers():                          # Функция перевода букв в числа

    global numeric_phrase
    global alphabet
    global num_list
    numeric_phrase=''
    num_list=[]

    for i in phrase:
        if i in alphabet:
            numeric_phrase+=str(alphabet.index(i)+1)
            numeric_phrase+=' '
            num_list.append(str(alphabet_list.index(i)+1))
        else:
            numeric_phrase+=i
            numeric_phrase+=' '
            num_list.append(i)
    print('В числах эта фраза выглядит так:',numeric_phrase)


def numbs_to_letts():                               # Функция перевода чисел обратно в буквы

    global numeric_phrase
    global alphabet
    global letter_phrase
    letter_phrase=''

    for k in num_list:
        if k in numbers_list:
            letter_phrase+=alphabet_list[int(k)-1]
        else:
            letter_phrase+=k

    print('Перевод обратно в буквы:',letter_phrase)

lett_to_numbers()           # Вывод числовой строки

numbs_to_letts()            # Вывод буквенной строки


