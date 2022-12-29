# Klass yaratib olamiz
class Car:
    def __init__(self, make, model, year, km=0, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.__km = km
        self.price = price

    def set_price(self, price):
        ''''narxini yangilaydi  '''
        self.price = price

    def add_km(self, km):
        '''km ga yana km qo'shadi'''
        if km >= 0:
            self.__km +=km
        else:
            raise ValueError('Musbat qiymat kiriting')

    def get_info(self):
        '''Mashina haqida ma'lumot qaytaradi'''
        info = f"{self.make.upper()} {self.model.title()} {self.year}-yil, {self.__km}km yurgan."
        if self.price:
            info += f"Narxi {self.price}"
        return info

    def get_km(self):
        '''mashina km ko'rsatasi'''
        return self.__km


