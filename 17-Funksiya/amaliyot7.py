"""
SUSAMBIL: author: Guni

Amaliyot7

"""

#foydalanuvchidan son qabul qilib sonning 2dan 10gacha qoldiqsiz bolinishini tekchiruvchi funksiya yozing va consolga chiqaring
def qoldiqsiz(son):
    '''2dan 10 gacha qoldiqsiz bolinadigan'''
    for s in range(2,11):
        if not son%s:
            print(f"{son} {s} ga qoliqsiz bo'linadi")

qoldiqsiz(8)