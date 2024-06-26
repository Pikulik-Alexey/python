# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284

def get_sum(n):
    sum = 1
    for el in range(2, n):
        # for el in range(2, n // 2 + 1):
        if n % el == 0:
            sum += el
    return sum


def get_friendlies(k):
    lst = []
    for n in range(1, k + 1):
        if n not in lst:
            m = get_sum(n)
            if get_sum(m) == n and n != m:
                lst.append(n)
                lst.append(m)
    return lst


print(get_friendlies(1000))
