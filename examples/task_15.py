# Функция получает на вход словарь с названием компаний в качестве ключа и списком с доходами и расходами в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, вернуть True, если убыточные - False.

data = {"company_1": [70, 12, 25, -28, 10, 36],
        "company_2": [-55, 10, -20, -10, 15, -15],
        "company_3": [40, 12, 21, -70, 11, 65]}


def func(data):
    for value in data.values():
        if sum(value) < 0:
            return False
    return True


print(func(data))
