import requests
from lxml import etree
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/116.0.5845.689 YaBrowser/23.9.5.689 Yowser/2.5 Safari/537.36"}
url = 'https://yandex.by/'
res = requests.get(url, headers=headers)
print(res.status_code)
tree = etree.HTML(res.content)
print(tree.xpath('/html/body/main/div[1]/a/@href')[0])
#  https://yandex.by/
