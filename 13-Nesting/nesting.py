# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:53:26 2022

@author: guni
NESTING

"""
#NESTING
car0 = {
        'model':'damas','rangi':'oq',
        'yil':'2018','narxi':'9000',
        'km':'5000','karobka':'avtomat'
        }

car1 = {
        'model':'nexi 3','rangi':'qora',
        'yil':'2000','narxi':'7000',
        'km':'7000','karobka':'mexanika'
        }

car2 = {
        'model':'gentra','rangi':'qizil',
        'yil':'2020','narxi':'20000',
        'km':'2000','karobka':'avtomat'
        }


cars = [car0, car1, car2]#lug'atlarni ro'yxat ichiga yuklaymiz
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rangi']} rang,"
          f"{car['yil']}-yilgi,{car['narxi']}$")


# BO'SH RO'YXATNI TO'LDIRISH for loop ni ishlatgan xolda
malibus = []

for m in range(10):
    new_car = {
        'model':'malibu',
        'rang':'None',
        'yil':'2022',
        'narx':'None',
        'km':'0',
        'korobka':'avto'}
    malibus.append(new_car)

# 1-uchtasiga qizil rang beramiz
for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

# keyingi 3 tasiga qora rang beramiz
for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'

#Oxirgai 4tasiga rangi qora karobkasiga mexanika beramiz
for malibu in malibus[6:]:
    malibu['rang'] = 'qora'
    malibu['korobka'] = 'mexanika'

# Karobkasiga qarab narx beramiz
for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narx'] = 40000
    else:
        malibu['narx'] = 35000

#Mashinalar ro'yxatini konsolga chaqiramiz
for malibu in malibus:
    print(malibu.values())


#LUG'AT ICHIDA RO'YXAT
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['pyton','php'],
    'maryam':['c++','c#']}

for ism,tillar in dasturchilar.items():# items() metodidan foydalanamiz
    print(f"\n{ism.title()}:", end='')
    for til in tillar:
        print(f'{til.title()} ', end='')

# LUG'AT ICHIDA LUG'AT (bunday qilish tavsiya etilmaydi!!!)
hamkasiblar = {
    'ali':{'familiya':'valiyev',
           'tyil':'1997',
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':'1995',
            'malumot':"o'rta maxsus",
            'tillar':['html','css'],
            },
    'hasan':{'familiya':'husanov',
             'tyil':'1999',
             'malumot':'maxsus',
             'tillar':['c#','python']
             }
    }

#quyidagicha malumotlarni ko'rish mumkin
for ism, info in hamkasiblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['tyil']}-yilda tug'ulgan.\n"
          f"Malumoti:{info['malumot']}. \n"
          "Quyudagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
