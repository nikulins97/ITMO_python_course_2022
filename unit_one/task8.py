#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
A = 10
B = 3
C = 7
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

# Пример 2:
A = 2
B = 10
C = 7
# Итоговый результат должен быть:
# A = 2
# B = 7
# C = 10
max_AB = A if A>B else B
min_AB = A if A<B else B
max_ABC = max_AB if max_AB>C else C
min_ABC = min_AB if min_AB<C else C
mid_ABC = A if A>min_ABC and A<max_ABC else C
mid_ABC = B if B>min_ABC and B<max_ABC else C
A = min_ABC
B = mid_ABC
C = max_ABC
print("A = ", A, "B =", B, "C =",C)
