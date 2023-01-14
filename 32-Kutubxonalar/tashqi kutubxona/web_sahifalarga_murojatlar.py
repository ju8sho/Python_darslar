# Avalam bor modulni o'rnatib olamiz (pip install requests)

import requests
from pprint import pprint

manzil = "https://kun.uz/news/main"
javob = requests.get(manzil)
pprint(javob.text)

