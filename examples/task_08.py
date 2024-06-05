# Напишите функцию, которая принимает строку текста.
# Сформулируйте список с уникальными Unicode каждого символа введенной строки отсортированный по убыванию
# решете через lc

def func(data):
    return sorted(set([ord(el) for el in data]), reverse=True)


print(func("rhgjoiiekd;xjuhblo"))
