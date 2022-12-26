"""
SUSAMBIL

funksiyalarni tekshirish

"""
# maskur funksiya
def get_full_name(ism, familya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familya}".title()
    else:
        return f"{ism} {familya}".title()


#print(get_full_name('alijon', 'valiyev'))


#Funksiyani tekshiruvchi dastur yozish
# name.py modulda