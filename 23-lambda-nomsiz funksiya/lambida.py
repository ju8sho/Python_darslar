"""
SUSAMBIL: author: Guni

Lambda - Nomsiz funksiya

"""

# lambida funksiya quyudagicha yaratiladi ;
#lambda argument:ifoda

import math

uzunlik = lambda pi , r :2*pi*r
print(uzunlik(math.pi, 1))

produkt = lambda x , y:x**y
print(produkt(3, 2))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def daraja(n):
    return lambda x : x**n
#daraja funksiyasidan yana 2ta funksiya yaratik
kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga teng")
print(f"3-ning kubi {kub(3)} ga teng")

# map()Funksiyasi
from math import sqrt
sonlar = list(range(11))#0dan 10gacha sonlar royxati
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

#>>>>>>>>>>>>>>>>>>>>>>>
sonlar = list(range(11))#0dan 10gacha sonlar royxati
def daraja1(x):
    '''Berilgan sonni kvadratini qaytaruvchi funksiya'''
    return x*x
print(list(map(daraja1,sonlar)))
#lambda funksiyasida
kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)
#>>>>>>>>>>>>>>>>>

a = [4,5,6]
b = [7,8,9]
a_pilus_b = list(map(lambda x ,y : x+y ,a,b))
print(a_pilus_b)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

ismlar = ['ali','vali','hasan','husan']
print(list(map(lambda matn:matn.upper(),ismlar)))

#Filter funksiya
import random
sonlar1 = random.sample(range(100),10)
def juftmi(x):
    return x%2==0

juft_sonlar = list(filter(juftmi,sonlar1))
print(sonlar1)
print(f"juft sonlar:{juft_sonlar}")

#lambda funksiyasi yordamida ko'ramiz
sonlar2 = random.sample(range(100),10)
juftsonlar = list(filter(lambda son:son%2==0,sonlar2))
print(sonlar2)
print(f"juft sonlar:{juft_sonlar}")

# .startswith() metodi
mevalar = ['olma','anjir','behi','nok','anor','banan','olxo\'ri','qovun']
mevB = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevB)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

mevalar1 = list(filter(lambda meva:len(meva)<=4,mevalar))
print(mevalar1)


#>>>>>>>>>>>>>>>>>>>>>>>
list(filter(lambda meva :(meva.startswith('a') and meva.endswith('r'),mevalar)))



