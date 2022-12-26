"""
SUSAMBIL: author: Guni

Amaliyot

"""

def kopaytma(*sonlar):
    '''Kiritilgan sonlarni ko'paytmasini qaytaradi'''
    yigindi = 1
    for son in sonlar:
        yigindi *=son
    return yigindi

print(kopaytma(2,3,6))