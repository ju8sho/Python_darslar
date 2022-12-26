# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:15:56 2022

@author: guni
"""

mahsulotlar = ['olma','kalbasa','piyoz','sabzi','go\'sht','shanpun','raptir','pastalar','non','sarog\'']
savat = []
print("kamida 5 ta maxsulot kiriting")
for sora in range(5):
    savat.append(input(f"{sora+1}-maxsulot:"))

for taom in savat:
    if taom in mahsulotlar:
        print(f"Do'konimizda {taom} bor")
    else:
        print(f"{taom} do'konda yo'q")
