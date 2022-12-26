"""
SUSAMBIL: author: Guni

Inkapsulyatsiya Klassga xos xususiyatlar va metodlar

"""

from uuid import uuid4
class Avto:
    """Avtomabil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        '''Avtomabilning xususiyatlari'''
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()

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

avto1 = Avto('GM', 'Malibu','Qora',2022,30000,100)
print(f"ID:{avto1.get_id()}")
print(f"KM:{avto1.get_km()}")
avto1.add_km(2000)
print(avto1.get_km())