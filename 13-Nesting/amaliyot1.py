# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:48:22 2022

@author: Guni
"""
# AMALIYOT

navoiy = {
    'ism':'Alisher Navoiy',
    'tyil':'1441',
    'kasb':'davlat arbobi',
    'asar':['xamsa','sakkiz jannat']
    }

gulom = {
    'ism':"G'afur G'ulom",
    'tyil':'1903',
    'kasb':'shoir',
    'asar':['guliston','shum bola']
    }

goipov = {
    'ism':'Davron Gaipov',
    'tyil':'1961',
    'kasb':"rock-n-rol qo'shiqchisi",
    'asar':['alambalo','alambalo']
    }

qahhor = {
    'ism':'Abdulla Qahhor',
    'tyil':'1907',
    'kasb':'yozuvchi',
    'asar':['sarob','olam yasharadi']
    }

adabiyot = [navoiy,gulom,goipov,qahhor]
for adabiy in adabiyot:
    ism = adabiy['ism']
    tyil = adabiy['tyil']
    kasb = adabiy['kasb']
    print(f"{ism} {tyil}-yilda tug'ulgan sohasi:{kasb}")
# 2-variant
    # print(f"{adabiy['ism'].title()}, "
    #       f"{adabiy['tyil']}-yilda tug'ulgan, "
    #       f"Kasbi:{adabiy['kasb']}")
for adabiy in adabiyot:
    ism = adabiy['ism']
    asar = adabiy['asar']
    print(f"\n{ism}-mashxur asarlari:")
    for a in asar:
        print(a.upper())
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
kinolar = {
    'ali':['marvel','dg'],
    'vali':['mistitel','kapitan amerika'],
    'vandam':['vandam','jumanji']}

for ism, kalit in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolar: ", end='')
    for k in kalit:
        print(f'{k.title()}. ',end='')

davlatlar = {
            'gabon':{'Markaziy Afrikadagi davlat.Maydon 267,7 ming km2. Aholisi 1,475 mln. kishi (2009).Poytaxti – Librevil shahar. Maʼmuriy jihatdan 9 viloyat (provinsiya)ga boʻlinadi.'
                     },
             'rossiya':{'moskva','km','None'
                        },
            }
#print(davlatlar['gabon']['poytaxt'])

user = input("\nistalgan davlat nomini kiriting:")

for davlat, info in davlatlar.items():
    if user in davlat:
        for malumot in info:
            print(malumot)
else:
    print("Hozircha bunday malumot yo'q!")






