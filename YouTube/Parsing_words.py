#  Парсинг 1000 существительных с сайта
from bs4 import BeautifulSoup
import requests

my_url = (
    'http://dict.ruslang.ru/freq.php?act=show&dic=freq_s&title=%D7%E0%F1%F2%EE%F2%ED%FB%E9%20%F1%EF%E8%F1%EE%EA%20%E8%EC%E5%ED%20%F1%F3%F9%E5%F1%F2%E2%E8%F2%E5%EB%FC%ED%FB%F5')
res = requests.get(my_url)  # res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
print(res.status_code)
tag_tr = soup.find_all("tr")[3:]
print(len(tag_tr))
with open('D:/my_data.txt', 'w', encoding='utf-8') as file:
    for el in tag_tr:
        a = el.find_all()
        file.write(a[2].text + "\n")
        # print(a[2].text)
