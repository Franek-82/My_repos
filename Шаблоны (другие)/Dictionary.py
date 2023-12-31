#    СЛОВАРИ
#  Сколько раз встречается каждое из чисел.
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
print(result)

# 2
result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
    # 2-ой аргумент get - значение, которое вернется, если заданного ключа нет.
print(result)

#  СортировкА словаря по значениям
capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

for key, value in sorted(capitals.items(), key = lambda x: x[1]):
    print(value)

#  создаем словарь на основе списка кортежей
info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
info_dict = dict(info_list)

#  Извлечение из словаря элементов с определенными ключами
dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]
dict2 = {k: dict1[k] for k in selected_keys}
print(dict2)