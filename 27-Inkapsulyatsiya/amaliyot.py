"""
SUSAMBIL: author: Guni

Amaliyot

"""

#Supper class
from uuid import uuid4
class Shaxs:
    '''Shazslar haqida ma'lumot'''
    __shaxs_soni = 0

    def __init__(self,ism,familya,passport,tyil):
        self.ism = ism
        self.familya = familya
        self.__passport = passport
        self.tyil = tyil
        self.__aydi = uuid4()
        Shaxs.__shaxs_soni += 1

    def get_id(self):
        '''Aydi raqamni ko'rsatadi'''
        return self.__aydi

    @classmethod
    def get_shaxs_soni(cls):
        return cls.__shaxs_soni

    def get_info(self):
        '''Shaxs haqida mal'umot'''
        info = f"{self.ism} {self.familya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ulgan ID:{self.__aydi}"
        return info

    def add_passport(self,passport):
        '''Shaxsning tyilini yangilaydi'''
        return self.__passport

    def get_age(self,yil):
        '''Shaxsning tug'ulgan yilini qaytaruvchi metod'''
        return yil - self.tyil


# inson0 = Shaxs('Olim','Olimov','DF12345678',1997)
# inson = Shaxs('Hasan','Hasanov','AA34677',1997)
# print(inson.get_num_shaxs())
# print(inson0.get_info())

class Talaba():
    '''Talaba klassi'''
    __talabalar_soni = 0
    def __init__(self,ism,familya,passport,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
        self.__aydi = uuid4()
        Talaba.__talabalar_soni +=1

    @classmethod
    def talaba_soni(cls):
        return cls.__talabalar_soni

    def get_id(self):
        '''Talabaning id raqami'''
        return self.idraqam

    def get_bosqich(self):
        '''Talabaning o'qish bosqishi'''
        return self.bosqich

    def get_info(self):
        info = f"{self.ism} {self.familya}."
        info += f"{self.get_bosqich()}-bosqich. ID:{self.get_id()}"
        return info

talaba1 = Talaba('Olim','Olimov','DF12345678',1997)
print(Talaba.talaba_soni())
