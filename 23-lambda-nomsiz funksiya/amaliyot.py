"""
SUSAMBIL: author: Guni

amaliyot

"""

kopaytma = lambda son: son*10
print(kopaytma(2))


yigindi = lambda a, b : a+b
print(yigindi(2, 5))


import random
sonlar = random.sample(range(1000), 10)
print(sonlar)

import math
kvadrat = list(map(lambda a :a*2,sonlar))
print(f"Kvadratlar {kvadrat}")

toq_son = list(filter(lambda son:son%3==0,sonlar))
print(f"toqsonlar{toq_son}")



