"""
SUSAMBIL: author: Guni

Amaliyot

"""

def fibonacci(a):
    sonlar = []
    for x in range(a):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
print(fibonacci(10))