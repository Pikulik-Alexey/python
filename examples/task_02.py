# Обойти четные элементы на нечетных позициях.

array = [10, 51, 32, 101, 157, 800, 200, 554]

for i in range(0, len(array), 2):
    if array[i] % 2 == 0:
        print(array[i])

print()
# четные позиции
for i in range(1, len(array), 2):
    if array[i] % 2 == 0:
        print(array[i])
