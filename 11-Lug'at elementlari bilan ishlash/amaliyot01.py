# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:51:13 2022

@author: guni
"""

#python izohli lugatini yarating kamida 10 ta so'zdan iborat bo'lsin.lugatdan kalit va qiymatni for loop yordamida alfbo ketma ketligida consolga chiqaringslovar = {'марафон': 'гонка бегунов длиной около 26 миль',
slovar = {'персона': 'человек',
'бежал': 'бежать в прошедшем времени',
'бежать': 'двигаться со скоростью',
'туфля': 'род обуви, закрывающей ногу не выше щиколотки',
'туфли': 'туфля во множественном числе',
'bir':'1',
'ikki':'2'}
for k ,q in sorted(slovar.items()):
    print(f"{k} - {q}.")


#Davlatlar va ularning poytaxtlarini lug'atini tuzing 1-davlatlar 2-poytaxtlarni alohida qilib chiqaring
davlatlar_poytaxtlar = {}
davlatlar_poytaxtlar['uzbekistan'] = 'tashkent'
davlatlar_poytaxtlar['rossiya'] = 'moskva'
davlatlar_poytaxtlar['aqsh'] = 'vashington'
davlatlar_poytaxtlar['qirg\'iziston'] = 'bishkek'
davlatlar_poytaxtlar['tojikiston'] = 'dushanbe'

print("\nDavlatalr:")
for davlat in sorted(davlatlar_poytaxtlar):
    print(davlat.upper())

print("\nPoytahtlat:")
for poytaxt in sorted(davlatlar_poytaxtlar.values()):
    print(poytaxt.upper())



user = input("Istalgan davlat nomini kiriting:").lower()

y = davlatlar_poytaxtlar.get(user)
if y == None:
    print("Kechirasiz bu xaqida malumaot yo'q")
else:
    print(y.upper())

#>>>>>
menu = {
        'osh':'15000',
        'sho\'rva':'20000',
        'manti':'18000',
        'dimlama':'28000',
        'mastava':'10000',
        'shashlik':'13000',
        'kebab':'25000',
        'non':'5000',
        'salat':'2500'}
buyurtma = []
print("3ta taom buyurtiring")
for b in range(3):
    buyurtma.append(input(f"{b+1}-taomni kiriting:"))

for b in buyurtma:
    if b in menu:
        print(f"{b} {menu[b]}")
    else:
        print(f"Bunday-'{b}' taom yo'q")
