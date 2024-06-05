# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > 0:
        return sum(a - 1, b + 1)
    return sum(a + 1, b - 1)


a = 2
b = 2
print(sum(a, b))


# def f_1(a, b):
#     while b != 0:
#         a += 1
#         b -= 1
#     return a


# print(f_1(2, 2))


# def f_2(a, b):
#     while b == 0:
#         return a
#     return f_2(a + 1, b - 1)


# print(f_1(2, 2))