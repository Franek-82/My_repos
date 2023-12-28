from bs4 import BeautifulSoup
import requests

my_url = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
res = requests.get(my_url)  # res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
#  print(res.status_code)
#  print(res.encoding)
print(soup.prettify())
