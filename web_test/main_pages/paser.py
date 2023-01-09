# beautiful로 파싱

import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://scholar.google.com/scholar?hl=ko&as_sdt=0%2C5&q=%EB%8C%80%EA%B5%AC%EA%B0%80%ED%86%A8%EB%A6%AD%EB%8C%80%ED%95%99%EA%B5%90+%EC%84%9C%EB%8F%99%EB%A7%8C&btnG=")
soup = bs(page.content, "html.parser")

print(soup)