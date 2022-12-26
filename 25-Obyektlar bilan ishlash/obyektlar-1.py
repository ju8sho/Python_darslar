"""
SUSAMBIL: author: Guni

Obyektlar bilan ishlash

"""
#Xususiyatlarga standart qiymat berish
class Talaba:
    '''Talaba nomli class'''
    def __init__(self,ism,familya,tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        self.bosqich = 1#standart qiymat beramiz

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
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #Standart qiymatni o'zgartirish
    def set_bosqich(self,bosqich):
        '''Talabani kursini yanglovchi metod'''
        self.bosqich = bosqich

    def update_bosqich(self):
        '''Talalabaning bosqishini 1 taga ko'paytiradi'''
        self.bosqich +=1

    def get_info(self):
        return f"{self.ism.title()} {self.familya.title()}. {self.bosqich}-bosqish talabasi."


talaba1 = Talaba('olim', 'olimov',1997)
talaba2 = Talaba('Vali', 'Valiyev',1995)
print(talaba1.get_info())#murojat etish
print(talaba2.get_info())


#Standart qiymatni o'zgartirish
talaba1.set_bosqich(4)#3-usuli
talaba2.update_bosqich()#4-usuli
talaba2.update_bosqich()#metodni xargal chaqirilganda 1taga qo'shib boradi
# #talaba1.bosqich = 2 # 1-usuli
# print(talaba1.get_info())
# print(talaba2.get_info())
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Obyektlar o'rtasida munosabatlar
class Fan():
    '''Fan nomli class. keyinchalik fanga nom beriladi'''
    def __init__(self,nomi):
        self.nomi = nomi#Fan nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def get_name(self):
        '''Fan nomi'''
        return self.nomi

    def add_student(self,talaba):
        '''Fanga talabalrni qo'shish'''
        self.talabalar.append(talaba)
        self.talabalar_soni  += 1

    def get_students(self):
        '''Fanimizga yozilgan talabalar malumotlari'''
        return [talaba.get_info() for talaba in self.talabalar]


matematika = Fan("Oliy Matematika")

talaba1 = Talaba('olim', 'olimov',1997)
talaba2 = Talaba('Vali', 'Valiyev',1995)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
print(matematika.talabalar_soni)
mat_talabalar = matematika.get_students()
print(mat_talabalar)



#Obyektning xususiyatlari va metodlarini ko'rish
#dir() funksiyasi
dir(Talaba)#  shu tarzda consolga yoziladi

#Dunder metotdalarni tashlab , bizga kerakli metodlarni qaytaruvchi funksiya
def see_methods(klass):
    '''Klassimizning kerakli metodini qaytaradi'''
    return[method for method in dir(klass) if\
            method.startswith('__') is False]
print(see_methods(Talaba))

# __dict__Metodi obyektlarning xususiyatlarini lug'at ko'rinishida qaytaradi
print(talaba1.__dict__)
#faqat kalitlarni ajratamiz
print(talaba1.__dict__.keys())