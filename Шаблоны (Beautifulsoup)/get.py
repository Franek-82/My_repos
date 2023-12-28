#  Метод get() в bs4 используется для получения значения атрибута элемента HTML.
from bs4 import BeautifulSoup
html = '<a href="https://example.com">Ссылка</a>'
soup = BeautifulSoup(html, 'html.parser')
link = soup.find('a')

href = link.get('href')  # Извлекает значение атрибута href
href2 = link['href']     # Извлекает значение атрибута href

print(href)   # Выводит https://example.com
print(href2)  # Выводит https://example.com

#  В bs4 также существует метод attrs, который возвращает словарь
# со всеми атрибутами элемента.
