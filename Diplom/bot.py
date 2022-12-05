import telebot
from telebot import types
import psycopg2

token="5880880630:AAF4khUIhV9QB_NhzT0PVIVdKT6VNnh5RhI"
bot=telebot.TeleBot(token)

# Вызов следующего id из txt-файла
c = open('current_id.txt', 'r')
current_id = int(c.readline())
c.close()


# Декоратор запуска бота

@bot.message_handler(commands=['start'])
def start_message(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Регистрация', callback_data='btn1')
    btn2 = types.InlineKeyboardButton(text='Получить данные об ID', callback_data='btn2')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, "Привет, вы запустили бота для регистрации!\nВы можете зарегистрироваться или узнать свой ID, если уже зарегистрированы.", reply_markup=kb)


# Декоратор обработки callback

@bot.callback_query_handler(func = lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        sent = bot.send_message(callback.message.chat.id, "Вы выбрали регистрацию.\nВведите ваше имя.")
        bot.register_next_step_handler(sent, db_write_name)

    if callback.data == 'btn2':
        ask_number = bot.send_message(callback.message.chat.id, "Вы выбрали ID\nУкажите ваш номер телефона")
        bot.register_next_step_handler(ask_number, db_read)


# Декоратор ответов на сообщения.

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Здравствуйте! Чем могу помочь?')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До встречи!')
    elif message.text.lower() == 'что ты умеешь?':
        bot.send_message(message.chat.id, 'Я помогу вам зарегистрироваться или узнать свой ID')
    elif message.text.lower() == 'я люблю python':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGrYVjjIzZoP_jAbT3-G013n7C6Wi8YgAC5AMAAonq5Qf3qStRjjmNnysE')
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGrYdjjI1LQIHfIFoslEDopwp4nBFV8wACJAADwZxgDEgkWrolDSiOKwQ')
        bot.send_message(message.chat.id, 'Пока что я не знаю, как ответить на ваше сообщение.')



# Блок функций


# Ввод имени
def db_write_name(message):
    global cl_name
    cl_name=message.text
    print(cl_name)

    sent = bot.send_message(message.chat.id, "Введите вашу фамилию")
    bot.register_next_step_handler(sent, db_write_surname)


# Ввод фамилии
def db_write_surname(message):
    global cl_surname
    cl_surname = message.text
    print(cl_surname)

    sent = bot.send_message(message.chat.id, "Введите номер телефона")
    bot.register_next_step_handler(sent, db_write_phone)


# Ввод номера телефона, занесение данных в БД
def db_write_phone(message):
    global current_id
    global cl_phone
    cl_phone = message.text
    print(cl_phone)

    try:
        conn = psycopg2.connect(database='registration', user='postgres', host='localhost', password='qwerty123')
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO clients (client_id, name, surname, phone)
                    VALUES (%(client_id)s, %(name)s, %(surname)s, %(phone)s);
                    """, {'client_id': current_id, 'name': cl_name, 'surname': cl_surname, 'phone': cl_phone})
        conn.commit()
        cur.close()
        conn.close()
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGra1jjJueSHLtqZw86GqG3aOxHIFNMgACHQIAArnzlwuzOvzMapbxQisE')
        bot.send_message(message.chat.id, 'Поздравляю, регистрация завершена успешно!\nМогу ли я ещё чем-то помочь?')

    except:
        bot.send_message(message.chat.id, 'Что-то пошло не так. Повторите попытку позже.')

    current_id+=1

    # Запись в файл нового id
    c = open('current_id.txt','w')
    c.write(str(current_id))
    c.close()


# Чтение id из БД
def db_read(message):
    phone_num = int(message.text)
    conn = psycopg2.connect(database='registration', user='postgres', host='localhost', password='qwerty123')
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    clients_data = cur.fetchall()

    try:
        for row in clients_data:
            print(row)
            if row[3] == str(phone_num):
                print(row[3], row[0])
                bot.send_message(message.chat.id, f"Ваш ID: {row[0]}")
    except:
        bot.send_message(message.chat.id, 'Пользователь с таким номером не найден')

    conn.commit()
    cur.close()
    conn.close()

bot.polling()