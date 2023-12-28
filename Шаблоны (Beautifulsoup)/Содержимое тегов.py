from bs4 import BeautifulSoup
import requests
my_url = 'http://example.com/'
res = requests.get(my_url)  # res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.head.title)     # <title>Example Domain</title>
print(soup.title)          # <title>Example Domain</title>
print(soup.find('title'))  # <title>Example Domain</title>

body_tag = soup.body
#  Содержимое тега <body> и его потомков
print('\n', body_tag, '\n')

#  Содержимое потомков <body>
print(list(body_tag.children))
