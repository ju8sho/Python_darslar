"""
SUSAMBIL: author: Guni

Funksiya

"""
#Funksiya yaratamiz
def salom_ber():
    """salom beruvchi funksiya"""
    print("Assalomu alaykum!")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Qiymat qaytaruvchi funksiya
def salom_beruvchi(ism):
    '''Foydalanuvchidan ism qabul qilib,
        unga salom beruvchi funksiya'''
    print(f"Assalomu alaykum,hurmatli {ism.title()}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Funksiyaga bir nechta argument uzatish
def toliq_ism(ism,familya):
    '''ism va familyani jamlab chiqaradi'''
    print(f"Ismi:{ism.title()}\n"
          f"Familyasi:{familya.title()}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#misol
# def yosh_hisobla(ism,tyil):
#     '''foydalanuvchini yoshini xisoblaydi'''
#     print(f"{ism.title()} {2022-tyil} yoshda")

#Paramet nomi bilan uzatush
#def yosh_hisobla(ism='olim',tyil=1999):
#    '''foydalanuvchini yoshini xisoblaydi'''
#    print(f"{ism.title()} {2022-tyil} yoshda")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Standart qiymat
def yosh_hisobla(t_yil,joriy_yil=2022):
    '''foydalanuvchini yoshini xisoblaydi'''
    print(f"Siz {joriy_yil-t_yil} yoshdasiz")

tyil= int(input("Tugulgan yilingizni kiriting:"))
yosh_hisobla(tyil)



