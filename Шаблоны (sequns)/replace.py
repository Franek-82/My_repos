# Функция для замены нескольких значений
def multiple_replace(target_str, dict_replace):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in dict_replace.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str


# создаем словарь со значениями и строку, которую будет изменять
my_dict = {"кот": "кошка", "кошка": "собака"}
my_str = "У меня есть кот и кошка"

# изменяем и печатаем строку
my_str = multiple_replace(my_str, my_dict)
print(my_str)
