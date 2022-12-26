
"""
Created on Sun Sep 18 20:26:11 2022

Ro'yxatlar bilan ishlash 08
@author: Guni
"""
#..alifbo bo'yicha tartiblash  .sort() metodi
cars = ['bmv','kiya','volvo','toyoto','gm','audi']
cars.sort()
print(cars)
#..list ichida katta xarif bo'lsa katta xarifni 1 ga qo'yadi
cars = ['bmv','kiya','volvo','toyoto','Gm','audi']
cars.sort()
print(cars)
#..teskari tartiblash .sort(revese = True)argumentidan
cars = ['bmv','kiya','volvo','toyoto','gm','audi']
cars.sort(reverse=True)
print(cars)
#..asl ro'yxat elementlarni buzmagan xolda tartiblash .sorted()funksiyasi
mevalar = ['Olma', 'behi','nok','anor','banan']
print("Sorted() qaytargan ro'yxat:",sorted(mevalar))
print("Asil ro'yxat o'zgarmas qoldi:",sorted(mevalar))
#.
print(sorted(mevalar, reverse=True))
#..
ages = [3,4,5,6,7,8,9,]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))
#..ro'yxatni aylantirish, boshini oxriga oxrini boshiga 
mevalar = ['Olma', 'behi','nok','anor','banan']
mevalar.reverse()
print(mevalar)
#..ro'yxatni uzunligini topish len()funksiyasi
cars = ['bmv','kiya','volvo','toyoto','Gm','audi']
print("Elementlar soni:",len(cars))
#..malum oralig'dagi sonlar ketma ketligi. range() funksiyasi
numbers = list(range(0,10))
print(numbers)
#..qadamlash
juft_solar = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print("Juft sonlar:",juft_solar)
print("Toq sonlar:",toq_sonlar)
#..max(),min(),sum() katta,kichik,yig'indi funksiyalar
narxlar = [1200,2000,1000,3000]
qimmat = max(narxlar)
arzon = min(narxlar)
jami = sum(narxlar)
print("Eng qimmat narx ",qimmat,\
      ". Eng arzon narx ",arzon,\
          ". Jami:",jami)
    
#..ro'yxatni kesish [:]
cars = ['bmv','kiya','volvo','toyoto','Gm','audi']
my_cars = cars[0:3]
print(my_cars)
print(cars[:4])#0dan boshlap oladi
print(cars[0:])#0dan boshlab oxrigacha oladi
print(cars[2:])
#..ro'yxatdan nusxa olish [:]to'liq ko'chirib olish
sonlar1 = [1,2,3,4,5]
sonlar2 =sonlar1[:]
sonlar2.append(6)
sonlar2.append(7)
print("Asil ro'yxat",sonlar1)
print("Nusxa olingan ro'yxat",sonlar2)
#..ozgarmas ro'yxatlar TUPLES
#bunday ro'yxatlarga ()odiy qavis ishlatiladi,shundan ajralib turadi
tomonlar = (20,45,5.6,78)#o'zgarmas ro'yxat
print(tomonlar)
print(tomonlar[0])
print(tomonlar[-1])
#o'zgartirish kiritib ko'ramiz
toys = ('bus','car','dino','lizart','dino')
#toys[3] = "isuzu"
#natijasi...>>
#TypeError: 'tuple' object does not support item assignment
#..agarda o'zgartirish talab qilinsa
#o'zgarmas ro'yxat yaratamiz..
toys = ('bus','car','dino','lizart','dino')
#o'zgarmas ro'yxatni odiy ro'yxatga aylantiramiz
toys =list(toys)
#ro'yxatga o'zgartirish kiritamiz
toys.append('isuzu')
toys.remove('car')
del toys[3]
toys[0] = 'otayol'
#ro'yxatni qytadan (tuple) ga aylantiramiz
toys = tuple(toys)
print(toys)