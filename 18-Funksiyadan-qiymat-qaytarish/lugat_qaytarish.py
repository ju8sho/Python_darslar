"""
SUSAMBIL: author: Guni

Funksiyadan lug'at qaytarish

"""

def avto_info(make,model,rang,karobka,yil,narx=None):
    avto = {'kompaniya':make,
            'model':model,
            'rang':rang,
            'korobka':karobka,
            'yil':yil,
            'narx':narx}
    return avto
avto1 = avto_info('GM','Malibu','Qora','Avtomat',2019)
avto2 = avto_info('GM','Gentra','Oq','mexanika',2022,40000)
avtolar = [avto1,avto2]
print("Onlayin bozordagi mashinalar:")

for avto in avtolar:
    if avto['narx']:#agar avtoda narx bolsa
        narx = avto['narx']
    else:
        narx = 'Noma\'lum'

    print(f"{avto['rang']} {avto['model']}.Narxi:{narx}")