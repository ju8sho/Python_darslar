"""
SUSAMBIL: author: Guni

class va obyektlar yaratish

"""
# klass yaratish
class Talaba:
    '''Talaba nomli class'''
    def __init__(self,ism,familya,tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil

# klassga metodlar qo'shish yoki funksiyalar
    def get_name(self):
        '''Talabaning ismini qaytaradi'''
        return self.ism

    def get_lastname(self):
        '''Talabaning familyasini qaytaradi'''
        return self.familya

    def get_fullname(self):
        '''Talabaning ismi va familyasini qaytaradi'''
        return self.ism,self.familya

    def get_age(self,yil):
        '''Talabaning yoshini qaytaradi'''
        return  yil - self.tyil


    def tanishtir(self):
        '''Talabaning malumotlari'''
        return f"Ismim {self.ism} {self.familya} {self.tyil}-da tug'ulganman"

#klassdan obyektlar yaratish
talaba1 = Talaba('Olim', 'Olimov', 1997)
talaba2 = Talaba('Vali', 'Valiyev',1995)
#klass obyektlariga murojat etish
print(talaba1.tanishtir())
print(talaba2.get_age(2022))

# pass OPERATORI
class User:
    '''User nomli class'''
    def __init__(self,name,username,email):
        self.ism = name
        self.nik = username
        self.email = email

#pass operatori [metod hali tayyor emas]
    def parol(self):
        '''Keyinroq metodni tayyorlash'''
        pass

    def email(self):
        '''Keyinroq metodni tayyorlash'''
        pass
