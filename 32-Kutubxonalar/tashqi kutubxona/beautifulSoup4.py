import requests
from bs4 import BeautifulSoup
from pprint import pprint


sahifa = "http://kun.uz/news/main"
r = requests.get(sahifa)
# pprint(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

#yangiliklarning mavzusini ajratib olamiz
news = soup.find_all(class_="news-title")

#eng biirinchi yangilikni consolga chiqaramiz
print(news[0].text)