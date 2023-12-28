#  После разбивки по сепаратору возвращается первый элемент
s = "ab.cd.ef"
a = s.split('.')[0]
print(a)

#   слова содержащие букву e
words = ['python', 'stepik', 'beegeek', 'iq-option']
new_words2 = list(filter(lambda w: 'e' in w, words))
print(new_words2)

# Если необходимо удалить только символы, которые есть в symbol
text = "abc _abc /def 1aaa"
symbol = "abc_/1"
text = "".join(el for el in text if el not in symbol)
print(repr(text))  # '  def '

# Если необходимо оставить в тексте только буквы и цифры
text = "".join(symbol for symbol in text if symbol.isalnum())
print(repr(text))  # 'def'
