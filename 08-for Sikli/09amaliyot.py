# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:23:08 2022

@author: user
"""

#5 ta elemendan iborar smlar degan ro'yxat tuzing
#va har bir elementga habar yozing takroran
ismlar = ['Ali','vali','hasan','husan','vandam']
for b in ismlar:
    print(f"Bugun man 'Macbook' oldim!{b}")
#yuqoridagi sikl tugaganidan so'ng cod n marta takrorlandi degan 
#habar chiqaring konsolga    
print(f"Kod:{len(b)} marta takrorlandi! ")  

#...
#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing
#ro'yxatning har bir elementi kubini yangi qatordan chiqaring
toq_sonlar = list(range(10,100,3))
for a in toq_sonlar:
    print(f"{a} ning kubi {a**3} ga teng")
#...    
#foydalanuvchidan 4 ta sevimli kinolarini kiritishini so'rang
#va kinolar degan ro'yxatga saqlab oling natijani konsolga chiqaring
print("4ta yoqtirgan kinolaringiz nomi")
kinolar = []
for k in range(4):
   kinolar.append(input(f"{k+1}-kino nomi?:")) 
print(kinolar)