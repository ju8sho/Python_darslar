# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 11:44:37 2022

@author: guni
"""

print("2 ta son kiriting")
son1 = int(input("1-son:"))
son2 = int(input("2-son:"))

if son1 == son2:
    pr = f"{son1}=={son2}"

if son1 < son2:
    pr = f"{son1}<{son2}"

elif son1 > son2:
    pr = f"{son1}>{son2}"

print(pr)



