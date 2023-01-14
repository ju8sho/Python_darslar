import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud


sahifa = "http://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')




