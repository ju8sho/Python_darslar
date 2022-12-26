# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:44:42 2022

@author: guni
"""

mahsulotlar = ['olma','kalbasa','piyoz','sabzi','go\'sht','shanpun','raptir','pastalar','non','sarog\'']
savat = []
print("kamida 5 ta maxsulot kiriting")
for sora in range(5):
    savat.append(input(f"{sora+1}-maxsulot:"))


bor_mahsulotlar = []
mavjutemas = []

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjutemas.append(mahsulot)

if mavjutemas:
    print("do'konimizda quyudagi mahsulotlar yo'q")
    for mahsulot in mavjutemas:
        print(mahsulot)
else:
    print("siz so'ragan mahsulotlar bor")