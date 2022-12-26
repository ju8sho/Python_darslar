"""
SUSAMBIL: author: Guni

Amaliyot2

"""
#Foydalanuvchidan son olib uning kubini va kvadratini hisoblovchi funksiya
def kub_kvadrat_xisobla(son):
    '''Foydalanuvchidan son olib uning kubini va kvadratini hisoblovchi funksiya'''
    print(f"Kiritilgan son:{son}= kvadtati:{son**2} ga kubi:{son**3} ga teng")

user = int(input("Istalgan son kiriting:"))
kub_kvadrat_xisobla(user)