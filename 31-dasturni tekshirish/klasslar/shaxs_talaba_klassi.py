class Shaxs:
    '''Shazslar haqida ma'lumot'''

    def __init__(self, ism, familya, passport, tyil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        '''Shaxs haqida mal'umot'''
        info = f"{self.ism} {self.familya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ulgan"
        return info

    def get_age(self, yil):
        '''Shaxsning tug'ulgan yilini qaytaruvchi metod'''
        return yil - self.tyil


class Talaba(Shaxs):
    '''Talaba klassi'''
    def __init__(self,ism,familya,passport,tyil,aydi):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familya,passport,tyil)#supper klassdan qancha,qanday xususiyatlarni olishini ko'rsatamiz
        #voris klass ga xos xususiyatla va metodlar
        self.idraqam = aydi
        self.bosqich = 1

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
