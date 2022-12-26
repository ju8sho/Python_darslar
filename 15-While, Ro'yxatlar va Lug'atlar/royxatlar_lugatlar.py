# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 18:53:07 2022

@author: guni
"""
#RO'YXAT TO'LDIRISH
print("Sinfdoshlar ro'yxatini tuzamiz")
ismlar = []
n = 1# ismlarni sanach uchun o'zgaruvchi

while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism kiritasizmi? (ha-yoq):")
    if javob =='ha':
        n+=1
        continue
    else:
        break
print("Ro'yxat tuzildi:",ismlar)

#LUG'AT TO'LDIRISH
print("Do'slaringiz yoshini saqlaymiz")
doslar = {}
ishora = True
while ishora:
    ism = input("Do'slaringiz ismini kiriting:")
    yosh = input(f"{ism.title()}ning yoshini kiriting:")
    doslar[ism] = int(yosh)

    javob = input("Yana kititasizmi ha/yoq?:")
    if javob == 'yoq':
        ishora = False

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#RO'YXAT ELEMENTLARINI O'CHIRISH
cars = ['lasetti','nexia','lasetti','damas','lasetti']

while 'lasetti' in cars:
    cars.remove('lasetti')
print(cars)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRICH
talabalar = ['ali','vali','hasan','husan']
talaba_baho = {}

while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting:")
    print(f"{talaba.title()} baholandi.")
    talaba_baho[talaba] = baho

