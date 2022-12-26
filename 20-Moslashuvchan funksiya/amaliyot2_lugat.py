"""
SUSAMBIL: author: Guni

Amaliyot

"""

def talabalar(ism,familya,**malumotlar):
    '''Kiritilgan malumotlarni lug'at ko'rinishida qaytarafi'''

    malumotlar['ism']= ism
    malumotlar['familya']= familya
    return malumotlar
talaba1= talabalar('Ali','Aliyev',yosh=25,tyil=1997)
talaba2= talabalar('Vali','Valiyev',yosh= 19,tugulgan_joy='Navoiy')
print(f"{talaba1}\n{talaba2}")