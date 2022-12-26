"""
SUSAMBIL: author: Guni

Modullarni chaqirib ishlash

"""
import avto

avto2 = avto.Avto('K', 'Kiya','Oq',2019,29900,20000)
print(avto2.get_km())

from avto import Bus
avto = Bus('UZ', 'Esuzu','Oq',2022,30000)
print(avto.get_info())