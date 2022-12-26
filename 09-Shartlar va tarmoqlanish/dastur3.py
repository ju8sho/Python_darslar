# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:05:13 2022

@author: guni
"""

foydalanuvchilar = ["admin",'guni','guni8','susambil','jumanazar']
log = input('yangi login kiriting:')

if log in foydalanuvchilar:
    print(f"Hush kelibsiz {log}:admin!")
else:
    print("boshqa login kiriting!")