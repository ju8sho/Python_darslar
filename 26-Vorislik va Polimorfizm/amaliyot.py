'''
Susambil
Amaliyot
'''


#Supper class
class Shaxs:
    '''Shazslar haqida ma'lumot'''
    def __init__(self,ism,familya,passport,tyil,manzil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
        self.manzil = manzil
    def get_info(self):
        '''Shaxs haqida mal'umot'''
        info = f"{self.ism} {self.familya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ulgan"
        return info

    def get_age(self,yil):
        '''Shaxsning tug'ulgan yilini qaytaruvchi metod'''
        return yil - self.tyil

# inson = Shaxs('Hasan','Hasanov','AA34677',1997)
# print(f"{inson.get_info()}.{inson.get_age(2022)} yoshda")

#Voris klass yaratish
class Talaba(Shaxs):
    '''Talaba klassi'''
    def __init__(self,ism,familya,passport,tyil,aydi,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familya,passport,tyil,manzil)#supper klassdan qancha,qanday xususiyatlarni olishini ko'rsatamiz
        #voris klass ga xos xususiyatla va metodlar
        self.idraqam = aydi
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []

    def fanga_yozil(self,fan):
        self.fanlar.append(fan)

    def get_id(self):
        '''Talabaning id raqami'''
        return self.idraqam

    def get_bosqich(self):
        '''Talabaning o'qish bosqishi'''
        return self.bosqich
#Polimorfizm - supper klass metodlarini qayta yozish
    def get_info(self):
        info = f"{self.ism} {self.familya}."
        info += f"{self.get_bosqich()}-bosqich. ID:{self.get_id()}"
        return info

# talaba1 = Talaba('Olim','Olimov','DF12345678',1997,'Fsd34683r4')
# print(talaba1.get_info())


class Manzil:
    '''Manzil saqlash uchun klass'''
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        '''Manzilni ko'rish'''
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} ko'chasi, {self.uy}-uy."
        return manzil

class Fan():
    '''Fan nomli klass'''
    def __init__(self,fanlar1):

        self.fanlar1 = fanlar1


fan1 = Fan('Onatili')
fan2 = Fan('Adabiyot')

fan1 = fan1.fanga_yozil(fan1)
