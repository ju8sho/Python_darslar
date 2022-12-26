# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:41:45 2022

@author: guni
"""
#Otam(uzi,aka,uka,o'rtoq) degan lug'at yarating va shu inson haqida malumaot kiriting va matin ko'rinishida consolga chiqaring
guni = {'ism':'guni','sharif':'guniboyev','t_yil':2022,'yosh':1}

print(f"{guni['ism'].title()} {guni['sharif'].title()} \
{guni['yosh']}-yoshda {guni['t_yil']}-yilda tug'ulgan")

#Oila azolaringizning sevimli taomlari lug'atini tuzing.lug'atda kamida 5 ta ism-taom juftligi bo'lsin,kamida 3 kishining sevimli taomini konsolga chiqaring
taom = {
        'bobur':'sho\'rva',
        'jasur':'konfet',
        'guni':'go\'sht',
        'sardor':'osh',
        'sevara':'salat'
        }
t = taom['guni']
print(f"Gunining sevimli taomi {t}")

#python izohli lug'at tuzing(pythondagi atamili modul,funksiya so'zlardan) kamida 10 ta kalit so'zdan iborat bo'lsin
python_lugat = {
    'print':'chop etish',
    'get':'mavjut emas',
    'append':'elementlar qo\'shish',
    'title':'har bir so\'zning bosh harifini katta harifga aylantiradi',
    'upper':'matindagi har bir hariflarni kattalashtiradi',
    'lower':'har bir harifni kichik harifga aylantiradi',
    'strip':'matinni boshi va ohridagi bo\'shliqni oladi',
    'lstrip':'matin boshidagi bo\'shliqni oladi',
    'rstrip':'matin oxridagi bo\'shliqni oladi',
    'input':'foydalanuvchidan so\'rash',
    'sort':'ro\'yxat elementlarini alifbo bo\'yicha tartiblaydi',
    'range':'malum bir oraliqdagi sonlarni shakilantiradi',
    'len':'elementlarning uzunligini aniqlaydi',
    'list':'malum bir oraliqni ro\'yxatini shakilantiradi'
    }

#foydalanuvchidan biror so'z kiritishini so'rang va so'zning tarjimasini yuqoridagilug'atdan chiqarib bering agar so'z lug'atda mavjut bo'lmasa "mavjut emas degan" habar chiqaring
# 1- variant
kalit = input("kalit so'z kiriting:")
print(python_lugat.get(kalit,'bunday so\'z mavjut emas'))

# 2-variant
kalit = input("kalit so'z kiriting:")
lugat = python_lugat.get(kalit)

if lugat == None:
    print("mavjut emas")
else:
    print(f"{kalit.upper()} so'zi {lugat}")
