# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
    "VI": " S005 "}, {"VII": " S005 "}, {"V": " S009 "}, {"VIII": " S007 "}]
set_1 = set()
for dict in list_dict:
    for value in dict.values():
        set_1.add(value)
print(set_1)

# сэт компрэхэншэн
# print({dict[item] for dict_1 in list_dict for item in dict_1})
