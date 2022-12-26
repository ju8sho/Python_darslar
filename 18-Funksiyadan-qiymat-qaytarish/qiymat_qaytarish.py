"""
SUSAMBIL: author: Guni

FUNKSIYADAN QIYMAT QAYTARISH

"""

#Funksiyadan yagona qiymat qaytarish
def toliq_ism_yasa(ism,familya):
    '''To'liq ism qaytaruvchi funksiya'''
    toliq_ism = f"{ism} {familya}"#local variables
    return toliq_ism

talaba1 = toliq_ism_yasa('olim', 'shamshiyev')
talaba2 = toliq_ism_yasa('vali', 'olimov')
print(f"Darsga kelgan talabalr:{talaba1.title()} va {talaba2.title()}")