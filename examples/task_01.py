a = 5
# цикл с условием
while a > 0:
    print(a)
    if a == 3:
        break
    a -= 1
else:
    print("Завершение цикла не по брейку")

my_str = "hlkfjsdlj"

for el in my_str:
    print(el, end=" ")

i = 0
while i < len(my_str):
    print(my_str[i], end=" ")
    i += 1