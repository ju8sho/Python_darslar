"""
SUSAMBIL: author: Guni

Klassning xususiyatlari va Metodlari

"""

from uuid import uuid4
class Bus:
    """Avtomabil klassi"""
    __num_avto = 0#Klass xususiyatlarini inkapsulyatsiya qilindi
    def __init__(self,make,model,rang,yil,narx,km=0):
        '''Avtomabilning xususiyatlari'''
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Bus.__num_avto += 1##inkapsulyatsiya qilindi
    #klassga oid metodlar
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        '''mashinaning km ga yana km qo'shamiz'''
        if km >= 0:
            self.__km += km
        else:
            return ("Mashina km ni kamaytirib bo'lmaydi")


avto2 = Bus('K', 'Kiya','Oq',2019,29900,20000)
#klass metodlariga klass nomi orqali murojat qilinadi
print(Bus.get_num_avto())

