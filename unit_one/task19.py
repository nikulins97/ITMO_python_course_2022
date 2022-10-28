#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

#Каждое значение из списка должно находится на отдельной строке.

#Тело программы

import csv

id=list(range(1,11))
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

my_file=open("new_table","wt", encoding='utf-8',newline="")
writer=csv.writer(my_file)
writer.writerows(zip(id,algoritm))

