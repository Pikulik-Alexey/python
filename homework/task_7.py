# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = 16
i = 0
degree = 1

while degree <= n:
    print(2 ** i)
    i += 1
    degree = 2 ** i