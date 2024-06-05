# Поменять последний элемент с первым
array = [10, 51, 32, 101, 157, 800, 200, 554]

last = array.pop()
first = array.pop(0)
array.insert(0, last)
array.append(first)
print(array)
