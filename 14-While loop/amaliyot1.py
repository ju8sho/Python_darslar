# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:48:28 2022

@author: guni
"""

print('\nYoqtirgan kitoblaringizni kiriting.')
user = '\nKitoblarni kiritib bo\'lgach (stop)ni kiriting:'
kitoblar = ''
ishora = True

while ishora:
    kitoblar = input(user)# shu kodni bajar qayta qayta
    if kitoblar == 'stop':
        ishora = False
    elif kitoblar == 0:
        print("Matin kiriting")
        continue
    else:print(kitoblar)
print("Dastur tugadi")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('Dasturni tugatish uchun "exit" deb yozing!')
user = 'Yoshingizni kiriting:'

while True:
    qiymat = input(user)
    if qiymat == 'exit' or qiymat =='quit':
        break

    yosh = int(qiymat)

    if yosh <7:
        narx = 2000

    elif 7<=yosh<18:
        narx = 3000

    elif 18<=yosh<65:
        narx = 10000

    else:narx = 0
    # solishtiramiz
    if narx == 0:
        print("Chipta bepul")
    else:
        print(f"Chipta narxi:{narx}so'm")
print('Dastur tugadi')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
savol = 'musbat son kiriting '
savol += 'dasturdan chiqish "exit":'

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break

    elif float(qiymat)<0:
        continue


    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")






