# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:37:33 2022
XATOLAR BILAN ISHLASH
@author: guni
"""
#TRY - EXCEPT (1- USLUB)
yosh = input('Yoshingizni kiriting:')
try:# blok ichida xato kelib chiqarishi mumkin bo'lgan cod
    yosh = int(yosh)
    print(f"Siz {2022-yosh}da siz")
except:#blok ichida xatolik yuz berganda bajaradigon cods
    print('Butun son kiriting')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#RTY-EXCEPT - ELSE (2- USLUB)
yosh = input('Yoshingizni kiriting:')

try:# blok ichida xato kelib chiqarishi mumkin bo'lgan cod
    yosh = int(yosh)#xato kelib chiqaruvchi cod

except:#blok ichida xatolik yuz berganda bajaradigon cods
    print('Butun son kiriting')#xato yuz berganda shu codni chiqar

else:#akis xolda javobni chiqar
    print(f"Siz {2022-yosh}da siz")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#MALUM TURDAGI XATOLARNI USHLASH
#ValueError
yosh = input('Yoshingizni kiriting:')
try:
    yosh = int(yosh)

except ValueError:
    print('Butun son kiritmadingiz')
else:
    print(f"Siz {2022-yosh}-yilda tug'ulgansiz")

IndexError
mevalar = ['olma','anor','bahi','nok']
try:
    print(mevalar[7])

except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#ZeroDivisionError
x,y = 5,10
try:
    y/(x-5)
except ZeroDivisionError:
    print('0 ga bo\'lib bo\'lmaydi')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Bir nechta xatolarni ushlash
n = input('Butun son kiriting:')
try:
    n = int(n)
    x=20/n
except ValueError:#agar butun son kiritmasa
    print('Butun son kiriting')
except ZeroDivisionError:#agar 0 kiritsa
    print('0 ga bo\'lib bo\'lmaydi')
else:
    print(f"x={x}")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#pass operatori xatolarni ko'rsatmaydi
yosh = int(input('Yoshingizni kiriting:'))
if yosh <20:
    pass
else:
    pass
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   isdigit()METODI sonlardan iborat ekanini tekshirish
while True:
    yosh = input('Yoshingizni kiriting:')
    if yosh.isdigit():
        yosh = int(yosh)
        break
print(f"Siz {2022-yosh}-yilda tug'ulgansiz")
