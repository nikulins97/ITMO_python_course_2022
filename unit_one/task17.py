#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество единиц товара.
#Цены хранятся в словаре:
prices = {"banana": 4,  "apple": 2,  "orange": 1.5,  "pear": 3}
def compute_bill():
    global prices
    val=list(prices.values())
    print('Список цен:',val)
    amount=list([int(input('Кол-во бананов:')), int(input('Кол-во яблок:')), int(input('Кол-во апельсинов:')), int(input('Кол-во груш:'))])
    print('Кол-во товаров:',amount)
    bill=0
    for i in range(0,len(val)):
        bill=bill+(val[i]*amount[i])
    print(bill)
compute_bill()



