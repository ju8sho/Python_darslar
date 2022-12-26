# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:52:02 2022

@author: guni
"""

mahsulotlar = []
buyurtma = "Buyurtma kiriting:"
while True:
    user = input(buyurtma)
    mahsulotlar.append(user)
    yana = input("Yana kiritsh uchun{ha}ni tugatish uchun entr:")
    if yana == 'ha':
        continue
    else: break
print("Buyurtma qilingan mahsulotlar:",mahsulotlar)
