# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:37:25 2022

@author: guni
 WHILE  LOOP(sikli)
"""

# son = 1
# while son <=10:#(toki) son 10dan kichik yoki teng ekan..
#     print(son, end='-')
#     son +=1#songa 1 ni qoshib boramiz
# print('dastur tugadi')
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # while va input
# print('\nKvadrat qiymatini qaytaradi')
# savol = "\nIstalgan son kiriting,"
# savol += "\nToxtash uchun 'stop' deb yozing!\n:"
# qiymat = ''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(float(qiymat)**2)
# print('Dastur tugadi etiboringiz uchun raxmat!')
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #  ISHORA - FLAG
# savol = "\nIstalgan son kiriting,"
# savol += "\nToxtash uchun 'stop' deb yozing!\n:"
# ishora = True
# while ishora:# toki ishora = True ekan
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # BREAK OPERATORI
# while True:# abadiy loop
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi etiboringiz uchun raxmat!')

# break for siklga xam ishlatiladi
sonlar = list(range(1,11))
for son in sonlar:
    if son ==5:
        break
    else:
        print(f"{son} ning kvadrati {son**2} ga teng!")

#CONTINUE OPERATORI
# for son in sonlar:
#     if son ==5:
#         continue
#     else:
#         print(f"\n{son} ning kvadrati {son**2} ga teng!")

son = 0
while son < 10:#toki son kichik ekan 10dan
    son += 1# songa 1 ni qo'shaver
    if son%2 !=0:# agar son toq bo'lsa
        continue
    else:
        print(son,end=' ')



