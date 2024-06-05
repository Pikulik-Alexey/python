# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# def f(a, b):
#     if a > 0 and b != 0:
#         return a ** b
#     return 0


# a = 3
# b = 5
# print(f(a, b))


# def f(a, b):
#     if b == 0:
#         return 1
#     return f(a, b - 1) * a


# a = 3
# b = 5
# print(f(a, b))

def func_1(a, b):
    res = 1
    for _ in range(b):
        res *= a
    return res


a = 3
b = 5
print(func_1(a, b))


# второй вариант
def func_2(a, b, res=1):
    if b == 0:
        return res
    return func_2(a, b - 1, res * a)


a = 3
b = 5
print(func_2(a, b))
