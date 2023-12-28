#  создание словаря с индексами списка
li = ['с', 'о', 'к', 'и']
d = {i: li[i] for i in range(len(li))}
print(d)

#  создание списка без индексов элементов списка "а"
a = [1, 3]
b = [element for i, element in enumerate(li) if i not in a]
print(b)

# создание генератора множеств
digits = {int(d) for d in '77abcd122ef78ghj90' if d.isdigit()}
print(digits)
