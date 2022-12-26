"""
SUSAMBIL: author: Guni

Funksiyadan ro'yxat qaytarish

"""

def oraliq(min,max,qadam=1):
    '''Berilgan sonlar oralig'ini shakilantiradi'''
    sonlar = []
    while min<max:
        sonlar.append(min)
        min +=qadam
    return sonlar

print(oraliq(0, 21,2))
