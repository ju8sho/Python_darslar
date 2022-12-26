# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:01:54 2022
LUG'AT ELEMENTLARII BILAN ISHLASH
@author: guni
"""
#.items()METODI
#bu metoda juftliklarni ko'rishimiz mumkin
car = {
       'model':'tiko',
       'color':'oq',
       'price':'25000',
       'year':'2007',
       'km':'48000'
       }
print(car.items())

#for sikli yordamida tushunarliroq qilgan holatda
for nomi ,qiymat in car.items():
    print(f"Nomi:{nomi}")
    print(f"Qiymati:{qiymat}")

#yana bir misol
telefonlar = {
    'ali':'iphone x',
    'vali':'samsung 20 pro',
    'hasan':'huawe p40 pro',
    'husan':'mi p30',
    'ali':'iphon x',
    'husan':'mi p30'
    }
for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}.")

#.keys()METODI (kalit)degan manoni beradi
#Bu metoda kalit so'zlarini topishda ishlatiladi
mahsulotlar = {
    'olma':'10000',
    'behi':'30000',
    'hurmo':'25000',
    'nok':'50000',
    'olcha':'47000',
    'banana':'15000',
    'anans':'27000',
    'glos':'18000'}
print(mahsulotlar.keys())
#for sikli ham ishlatishimiz mumkin
print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# misol
slovar = {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}

print(slovar.items())
#for loop yordamida
for s, l in slovar.items():
      print("{}-='{}'".format(s ,l))

     #Ro'yxat va Lug'at
#for loop va if shartlari yordamida

bozorlik = ['olma','olcha','nok','baliq','non','asal']
#solishtiramiz
for m in mahsulotlar:
    if m in bozorlik:
        print(f"{m.title()} {mahsulotlar[m]} so'm ")
#####################################
# not in operatori bilan
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Kechirasiz bizda {buyum} yo'q!")

#.sorted() funksiyasidan foydalanamiz alfavit bo'yicha chiqaramiz
print("Do'konimizdagi mahsulotlar")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

#.volues()METODI
from lugat_elementlari_bilan_ishlash import slovar
print(slovar.values())
print(len(slovar.values()))
#for loop yordamida
print("Slovar ichda 4 ta elemant bor ular quyudagilar:")
for s in slovar.values():
    print(s)

# set(FUNKSIYASI) bilan
# misol uchun biror bir lug'atni chaqirib olamiz
from lugat_elementlari_bilan_ishlash import telefonlar
# telefonlar lug'atida 2 martadan yozilgan elementlar bor!set()orqali sartirofka qilamiz
print(telefonlar)
print("Foydalanuvchilar quyidagi tel ishlatadilar!")
for tel in set(telefonlar.values()):
    print(tel)
# yana bir misol
mevalar = {
    'olma':'taram',
    'uzum':'shulg\'ayni',
    'banan':'sariq',
    "olma":'taram',
    'anjir':'shirin',
    'qalanpir':'achiq'
    }

print(sorted(mevalar.values()))