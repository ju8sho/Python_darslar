# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:40:43 2022

@author: guni
"""

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


