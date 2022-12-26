# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:57:34 2022

@author: guni
"""

bozor = {}
ishora = True
while ishora:
    nom = input('Mahsulot nomi:')
    narx = input(f"{nom.title()}ning narxi:")
    bozor[nom] = int(narx)

    javob = input("Tugtish uchun[yoq]kiriting:")
    if javob == 'yoq':
        ishora = False
print(bozor)