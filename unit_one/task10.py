# todo: 10.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 10.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.
A = float(input("Введите целое число А:"))
if A%1==0:
    print(bool(A%2==0))
else:
    print("Введено нецелое число")

