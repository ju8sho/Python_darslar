"""
SUSAMBIL: author: Guni

Funksiyalarni siklda ishlatish

"""

def avto_info(konpaniya,model,rang,karobka,yil,narx=None):
    avto = {'kompaniya':konpaniya,
            'model':model,
            'rang':rang,
            'korobka':karobka,
            'yil':yil,
            'narx':narx
            }
    return avto



avtolar = []
while True:
    print("\nQuyidagi malumotlarni kiriting", end=' ')
    konpaniya = input("\nIshlab chiqaruvchi: ")
    model = input("Modeli: ")
    rang = input("Rangi: ")
    korobka = input("Korobkasi: ")
    yil = input("Yili: ")
    narx = input("Narxi: ")
    #Kiritilgan ma'lumotlardan avto_info funksiyamiz yordamida
    #lug'at shakilantirib ,ro'yxatga qo'shamiz
    avtolar.append(avto_info(konpaniya, model, rang, korobka, yil,narx))

    #Yana avto qo'shish qo'shmasligini soraymiz
    javob = input("Yana avto qo'shasizmi? (yes/no):")
    if javob == 'no':
        break


print("Bozordagi mavjut avtomabillar:")
for avto in avtolar:
    if avto['narx']:#agar avtoda narx bolsa
        narx = avto['narx']
    else:
        narx = 'Noma\'lum'
    print(f"{avto['rang'].title()} {avto['model'].title()} .Narxi:{narx}")




