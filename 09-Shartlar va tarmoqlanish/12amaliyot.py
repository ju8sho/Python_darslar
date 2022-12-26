# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:29:44 2022

@author: guni
"""

yosh = int(input("Yoshingizni kiriting:"))
if yosh <=4 or yosh > 60:
    price = 0
elif yosh < 18:
    price = 10000
elif yosh > 18:
    price = 20000
print(f"Sizga chipta {price} so'm")



