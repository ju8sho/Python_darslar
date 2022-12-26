"""
SUSAMBIL: author: Guni

Amaliyot

"""

def katta_harf(matn):
    matn = matn[:]#funksiyaga kiritilayotgan qiymatdan nusxa olamiz
    for m in range(len(matn)):
        matn[m]= matn[m].title()
    return matn

matinlar= ['ali vali','aka uka']
yangi_ism= katta_harf(matinlar)
print(matinlar)
print(yangi_ism)