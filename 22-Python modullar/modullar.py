"""
SUSAMBIL: author: Guni

 Python Modullar

"""
import math

#math moduli hisob kitob bajaruvchi funksiyalar,o'zgaruvchilar joylashgan
# sqrt() funksiyasi kvadrat ildizni qaytaradi
a = 400
print(math.sqrt(a))

# pow(x,n) x ning n-darjasini qaytaruvchi funksiya
print(math.pow(5,2))


#>>>>
from math import pi

print(pi)

# random moduli
import random

son = random.randint(0, 100)
print(son)

# choice()funksiyasi berilgan argumentning ichidantasodifiy elementni qaytardi

ismlar = ['olim','ali','vali','hasan','husan','vandam','bobur','sardor','malika','valijon','akmal']
ism = random.choice(ismlar)
print(ism)#tasodifiy 1ta ism qaytaradi

a = list(range(0,51,5))
print(a)
print(random.choice(a))#tasodifiy 1ta son qaytaradi

# shuffle(x) funksiyasi x ichidagi elementlarni tasodifiy aralashtiradi
x = list(range(11))
print(x)
random.shuffle(x)#aralashtiramiz
print(x)

# sample(a,b) a ro'yxat ichidan tasodifiy k ta element ajratib oladi
from random import sample
a = list(range(0,100))#0dan 100gacha sonlar oraliq ro'yxati
b = sample(a,k=10)#ro'yxatdan 10 ta element ajratib oldadi
print(b)




