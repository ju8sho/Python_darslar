"""
SUSAMBIL: author: Guni

Modullar

"""

def avto_info(kompaniya,model,rang,karobka,yil,narx=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rang,
            'korobka':karobka,
            'yil':yil,
            'narx':narx
            }
    return avto
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def avto_kirit():
    '''Foydalanuvchiga avto_info funksiyasiyordamida bir nechta avtolar haqida malumotlarni bita ro'yxatga joylaydi'''
    avtolar = []
    while True:
        print("\nQuyidagi malumotlarni kiriting", end=' ')
        kompaniya = input("\nIshlab chiqaruvchi: ")
        model = input("Modeli: ")
        rang = input("Rangi: ")
        korobka = input("Korobkasi: ")
        yil = input("Yili: ")
        narx = input("Narxi: ")
        #Kiritilgan ma'lumotlardan avto_info funksiyamiz yordamida
        #lug'at shakilantirib ,ro'yxatga qo'shamiz
        avtolar.append(avto_info(kompaniya, model, rang, korobka, yil,narx))

        #Yana avto qo'shish qo'shmasligini soraymiz
        javob = input("Yana avto qo'shasizmi? (yes/no):")
        if javob == 'no':
            break
    return avtolar
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def info_print(avto_info):
    '''Avtolar xaqida malumotlar saqlangan lug'atni konsolga chaqirasi'''
    print(f"{avto_info['rang'].title()} "
          f"{avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, "
          f"{avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narx']}$")


