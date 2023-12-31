a = '\nasd\n\n'
b = '\r'
c = ' abc'
d = ''
e = '\n\n\n'
text = '\n     Hel lo  Wor   ld  !'
print(text.isprintable())
print(a.isspace())
print(b.isspace())
print(c.isspace())
print(d.isspace())

li = [a]
print(a)
print(li)
print(*li)

print(a.rstrip('\n'))
print("Строка е: ", e.rstrip('\n'))
print(c[-1])

#  Замена всех символов "1" в строке
s = '1 2 1 1 3 4 2'
a = s.replace('1', '')
print(repr(a))  # ' 2   3 4 2'
print(len(a))  # 10
