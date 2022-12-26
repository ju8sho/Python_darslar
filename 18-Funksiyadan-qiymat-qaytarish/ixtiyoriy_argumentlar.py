"""
SUSAMBIL: author: Guni

IXTIYORIY ARGUMENT

"""
#ixtiyoriy parametir qo'shish uchun: =''
def toliq_ism_yasa(ism,sharif,otasini_ismi=''):
    '''Toliq ism qaytaruvchi funksiya'''
    if otasini_ismi:#agar otasini ismi bo'lsa
        toliq_ism = f"{ism} {otasini_ismi} {sharif}"
    else:#akis holda
        toliq_ism = f"{ism} {sharif}"
    return toliq_ism.title()#ichki ozgaruvchina qaytar(return)

talaba1 = toliq_ism_yasa('olim', 'shamshiyev')
talaba2 = toliq_ism_yasa('vali', 'olimov','hasanov')
print(f"Darsga kelmagan talabalar:{talaba1} va {talaba2}")
