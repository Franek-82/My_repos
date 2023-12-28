from urllib.request import urlopen
from lxml import etree
url = 'http://example.com/'
page = urlopen(url)
html_code = page.read().decode('utf-8')
tree = etree.HTML(html_code)
print(tree.xpath("/html/body/div/p[2]/a/@href")[0])
#  https://www.iana.org/domains/example

#  Чтобы узнать путь к ссылке, надо в консоли браузера кликнуть на элементе "копировать",
#  затем выбрать "копировать XPath" и добавляем "/@href")[0]".
#  Если @href заменить на text(), программа вернет текст ссылки, а не сам URL.

#  <html>
#  <body>
#  <div>
#     <h1>Example Domain</h1>
#     <p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>
#     <p><a href="https://www.iana.org/domains/example">More information...</a></p>
#  </div>
#  </body>
#  </html>
