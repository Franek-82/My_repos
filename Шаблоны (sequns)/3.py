#  Найти символ который встречается чаще всего в строке
s = 'водолаз, майка'
most_common = s[0]
for el in s:
    if s.count(el) >= s.count(most_common):
        most_common = el
print(most_common)

#  Нахождение в строке кол-ва различных слов
s = input().lower()
my_set = set()
for i in s.split():
    if not i.isalnum(): #  забыл про strip()
        for j in ".,;:-?!":
            if i.endswith(j):
                i = i[:-1]
            if i.startswith(j):
                i = i[1:]
    my_set.add(i)
print(len(my_set))

#  2
words = [word.lower().strip('.,;:-?!') for word in input().split()]
print(len(set(words)))