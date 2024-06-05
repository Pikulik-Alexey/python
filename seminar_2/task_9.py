# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# 5! = 1 * 2 * 3 * 4 * 5

num = 5
fact = 1

while num > 1:
    fact *= num
    num -= 1
print(fact)

for el in range(1, num + 1):
    fact *= num
print(fact)


def factorial(num, f=1):
    if num == 0:
        return fact
    return factorial(num-1, f*num)

print(factorial(num))