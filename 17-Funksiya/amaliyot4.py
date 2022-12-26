"""
SUSAMBIL: author: Guni

Amaliyot4

"""

#Foydalanuvchidan 2 ta son olib ulardan kattasini consolga chiqaruvchi funksiya agar sonlar teng bo'lsa 'teng ekan'  degan habar chiqsin
def sonni_solishtir(a,b):
    '''Foydalanuvchidan 2 ta son olib ulardan kattasini consolga chiqaruvchi funksiya agar sonlar teng bo'lsa 'teng ekan'  degan habar chiqsin'''
    if a>b:
        print("{}>{}".format(a,b))
    elif a<b:
        print("{}<{}".format(a,b))
    else:
        print(f"{a}={b}")

sonni_solishtir(2, 3)
sonni_solishtir(45, 23)
sonni_solishtir(233*2, 345*4)
