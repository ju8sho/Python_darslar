"""
SUSAMBIL: author: Guni



"""
#klass yaratamiz
class User:
    '''Foydalanuvchi User klassi'''
    def __init__(self,ism,familya,nik,email,parol):
        self.name = ism
        self.familya = familya
        self.username = nik
        self.email = email
        self.parol = parol

#metod qoshamiz

    def get_name(self):
        '''Foydalanuvchini ismini qaytaradi'''
        return self.name

    def get_fullname(self):
        '''Foydalanuvchi ismi va familyasini qaytaradi'''
        return f"{self.name} {self.familya}"

    def get_tyil(self,tyil):
        '''Foydalanuvchini tug'ulgan yilini qaytaradi'''
        return tyil
#hali tayyor emas
    def email(self):
        pass
    def parol(self):
        pass
#
    def get_info(self):
        '''User malumotlarini qaytaradi'''
        return f"Foydalanuvchi:{self.username}, ismi:{self.name.title()} {self.familya.title()} email:{self.email}"

#klassdan obyekt yaratish

foydalanuvchi1 = User('olim','olimov','olimbek','olim0olimov@gmail.com','asd123asd')
foydalanuvchi2 = User('vali', 'valiyev', 'valleriya', 'vali123@gmail.com','12345fj5')


#klass obyektlariga murojat qilish
print(foydalanuvchi1.get_info())

print(foydalanuvchi2.get_info())

print(foydalanuvchi2.get_tyil(1997))

print(foydalanuvchi2.get_fullname().upper())

