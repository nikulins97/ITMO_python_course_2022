#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.

# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.


encoded_text="grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"
alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet_list=[let for let in alphabet]
indexes=list(range(1,27))


def decoding():                         # Функция декодинга
    global decoded_string
    decoded_string=''
    for shift in indexes:
        for i in encoded_text:
            if i in alphabet:
                if alphabet_list.index(i)+shift<26:
                    decoded_string+=alphabet_list[alphabet_list.index(i)+shift]
                else:
                    decoded_string+=alphabet_list[shift+alphabet_list.index(i)-26]
            else:
                decoded_string+=i
        print(shift, decoded_string)
        decoded_string=''

decoding()