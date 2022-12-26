# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:58:09 2022

@author: guni
"""
mahsulotlar = ['husan', 'hasan', 'vali', 'ali']

bozor = {'husan': '4', 'hasan': '4', 'vali': '5', 'ali': '3'}

while mahsulotlar:
    mahsulot = mahsulotlar.pop()
    if mahsulot in bozor.keys():
        narx = bozor[mahsulot]
        print(mahsulot,narx)
    else:
        print("xato")
