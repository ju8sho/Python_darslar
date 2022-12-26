"""
SUSAMBIL: author: Guni

Amaliyot

"""

class Avto:
    '''Avto nomli klass'''
    def __init__(self,modul,nomi,rang,karobka,yil,narx):
        self.modul = modul
        self.nom = nomi
        self.rang = rang
        self.karobka = karobka
        self.yil = yil
        self.narx = narx
        self.km = 0

    def get_modul(self):
        '''Modulini qaytaradi'''
        return self.modul

    def get_rang(self):
        '''Rangini qaytaradi'''
        return self.rang

    def get_karobka(self):
        '''Karobkasini qayteradi'''
        return self.karobka

    def get_yil(self):
        '''Mashinaning qaysi yilda chiqanini qaytaradi'''
        return self.yil

    def get_narx(self):
        '''Mashinaning narxini qaytaradi'''
        return self.narx

    def get_info(self):
        '''Mashina xaqidagi malumotlarni qaytaradi'''
        return f"{self.rang.upper()}:{self.nom.upper()}-[{self.modul.upper()}], chiqarilgan sana:{self.yil}\
            karobkasi:{self.karobka},klometryaj:({self.km}) narxi:{self.narx}$ "

#xususiyatlarini o'zgartiradigan metodlar

    def set_km(self,km):
        '''Mashinaning km ni o'zgartiadi'''
        self.km = km

    def update_km(self,km):
        '''hargal chaqirilganda km qo'shib boradi'''
        self.km = km*1

# print(avto1.get_info())

class Avtosalon:
    '''Avtosalon nomli klass'''
    def __init__(self,salon_nomi,adres,sotuvdagilar):
        self.nomi = salon_nomi
        self.sotuvdagilar = sotuvdagilar
        self.adres = adres
        self.sotuv_cars = []

    def add_cars(self,avtolar):
        '''Avtosalonga avtolar qo'shadi'''
        self.sotuv_cars.append(avtolar)

    def get_name(self):
        return self.nomi

    def get_sotuvdagi(self):
        return self.sotuvdagilar

    def get_adres(self):
        return self.adres

    def get_info_salon(self):
        '''Avtosalondagi avtomobillar haqida malumot'''
        return [x.get_info() for x in self.sotuv_cars]

    def salon_info(self,salon):
        return f"Salon nomi:{self.nomi} manzil:{self.adres} sotuvdagi avtomabillar:{self.sotuvdagilar}"


salonname = Avtosalon("Paradox Cars",'Namangan shaxaar,Pop tumani 9-uy',['malubi','kiya','damas'])
print(salonname.salon_info(salonname))
avto1 = Avto('gm','malibu','qora','avtomat','2022',45000)
avto2 = Avto('kl','kiya','qizil','mexanika',2019,23000)
avto3 = Avto('dw','damas','oq','mexanika',2020,9000)

avto1.update_km(100)
avto3.set_km(1200)

salonname.add_cars(avto2,)
salonname.add_cars(avto3)
salondagilar= salonname.get_info_salon()
print(salondagilar)
print(salonname.get_name())

#dict metodiga
def dikt_metodi(obyekt):
    return [metod for metod in dir(obyekt) if metod.startswith('__') is False]
print(dikt_metodi(avto1))





