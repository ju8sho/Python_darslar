# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 07:24:02 2022
             Lug'at va to'plam
@author: guni
"""
#lug'at yarataish
car = {'model':'ferrari','rang':'qora'}#madeli ferrari rangi qora

#lugatlar bilan ishlash
car = {'model':'ferrari','rang':'qora'}
print(car['model'])
print(car['rang'])

talaba = {'ism':'murod olimov','yosh':20,'t_yil':1998}
print(f"{talaba['ism'].title()},\
{talaba['t_yil']}-yilda tug'ulgan,\
{talaba['yosh']} yoshda")

#bir nechta qatorga bo'lib yozish
car = {
       'make':'GM',
       'model':'Malibu',
       'color':'black',
       'gear':'Automatic',
       'year':2022,
       'price':40000
       }

# .get() metodi
narx = car.get('narx','bunday kalit mavjut emas')
print(narx)
narx = car.get('narx')
print(narx)

#yangi juftlik qo'shish
talaba = {'ism':'murod olimov','yosh':20,'t_yil':1998}

talaba['kurs'] = 4
talaba['fakultet'] = 'informatika'
print(talaba)

#bo'sh lug'at
mashina = {}

#bo'sh ro'yxatni to'ldirish
mashina['model']='Mazde 7'
mashina['color']='Black'
mashina['price']=40000
print(f"{mashina['color']} {mashina['model']},{mashina['price']}$")

#qiymatni o'zgartirish
mashina['price']=35000
print(f"{mashina['color']} {mashina['model']},{mashina['price']}$")

#lug'atdagi elementlarni del operatori yordamida o'chirish
del mashina['color']


