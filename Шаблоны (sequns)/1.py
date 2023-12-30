#  Нахождение символов, которые повторяются
string = "Hello world"
dublic = set([el for el in string if string.count(el) > 1])
print(dublic)

#  2 Можно и строки и список
word_x, word = list("газета"), "арбуз"
print(set(word).intersection(word_x))

#  Метод replace в списочном выражении
str_list = ["кот", "собака", "кот собака", "кот кот"]
result_list = [elem.replace("кот", "кошка", 1) for elem in str_list]
print(result_list)  # Выведет ['кошка', 'собака', 'кошка собака', 'кошка кот']

#  удаление во множестве небуквенных символов
set_m = set('asd,g?ty.qwety!')
print(set_m.difference("'!?:-—/.,'"))

#  Цвет текста в консоли
print("\033[36m asdfg")  # бирюзовый
print("\033[31m asdfg")  # красный
