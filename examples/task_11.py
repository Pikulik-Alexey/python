# Функция принимает на вход три списка одинаковой длины:
# имена str
# ставка int
# премия str с указанием процентов вида "10.25"
# вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма расчитывается как ставка умноженная на процент премии


def func(names, salaries, awards):
    return {name: salary * float(award.rstrip('%')) / 100 for name, salary, award in zip(names, salaries, awards)}


names = ['Вася', 'Маша', 'Петя', 'Валера']
salaries = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85']

print(func(names, salaries, awards))
