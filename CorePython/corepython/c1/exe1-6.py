import re

import requests

html = requests.get('http://www.sina.com.cn/')
print(html.text)
m = re.findall(r'www.\w+.(?:com.cn|cn|edu|net|com)', html.text)
print(set(m))
