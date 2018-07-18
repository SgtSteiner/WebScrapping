import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.panel.es/desarrollo-de-software/")

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())
ar = soup.find_all('p')
for line in ar:
    print(line)
