# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:48:40 2022

@author: guni
"""

ranglar ={'qora','ola','sariq'}
ranglar.add('qizil')

ranglar.update(['yashil','oq',"ko'k",'pushti'])
print(ranglar)


set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
#umumiy elementlar
print(set1&set2)
set3 = {40, 50, 30}#umumiy elementlar set1 va set2 dan

#faarqini aniqlash
print(set1-set2)
print(set2.intersection(set1))

#simmetrik farq
print(set1^set2)
print(set1.symmetric_difference(set2))




bozorlik = ['choy','non','kartoshka','tuxum','sut']
mahsulot = ['non','sut','tuxum','olma','un','tuz']

bor = []
mavjut_emas = []

for b in bozorlik:
    if b in mahsulot:
        bor.append(b)
    else:
        mavjut_emas.append(b)

mahsulot.append('kartoshka')
mahsulot.append('choy')
print(mahsulot)
