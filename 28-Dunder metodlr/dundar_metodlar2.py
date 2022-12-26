"""
SUSAMBIL

dunder metodlar2

"""

class Avto:
    __num_avto =0
    def __init__(self,make,model,rang,yil,narx):
        '''Avtomabilning xususiyatlari'''
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx

    def __repr__(self):
        '''Obyekt xaqida ma'lumot'''
        return f"Avto:{self.rang} {self.make} {self.model}"
    #taqoslash uchun metodlar
    def __eq__(self,boshqa_avto):
        '''Tenglik'''
        return self.narx == boshqa_avto.narx

    def __lt__(self, boshqa_avto):
        '''Kichik'''
        return self.narx < boshqa_avto.narx

    def __le__(self, boshqa_avto):
        '''Kichik yoki teng'''
        return self.narx <= boshqa_avto.narx

class AvtoSalon:
    '''Avto salon klassi'''
    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    #len metodi
    def __len__(self):
        return len(self.avtolar)

    #getitame metodi
    def __getitem__(self, index):
        return self.avtolar[index]

    #obyekt elementlarini o'zgartirish[metod yozamiz]
    def __setitem__(self, index, value):
        if isinstance(value, Avto):
            self.avtolar[index] = value
            
    #Obyektlarni chaqirish
    
    #parametrsiz chaqirish
    # def __call__(self):
    #     return [avto for avto in self.avtolar]
    
    #parametr bilan chaqirish
    #yangi avto obyektni salonga qo'shib chiqaylik
    def __call__(self, *parametr):
        if parametr:# ager qiymat kiritilgan bo'lsa
            for avto in parametr:
                self.add_avto(avto)
        else:#ager qiymat bolmasa
            return [avto for avto in self.avtolar]
        
    #qo'shish metodi
    def __add__(self,parametr):
        if isinstance(parametr, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {parametr.name}")
            yangi_salon.avtolar = self.avtolar + parametr.avtolar
            return yangi_salon
        elif isinstance(parametr,Avto):#agar kiritilgan parametr Avto klassidan bo'lsa
            self.add_avto(parametr)#avtolar ro'yxatiga qo'sh
        else:
            print(f"AvtoSalonga {type(parametr)} qo'shib bo'lmaydi")
            
        
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")

#avtosalonga nom beramiz
salon1 = AvtoSalon('MaxAvto')
salon2 = AvtoSalon('Avto Lider')

#obyektlar yaratamiz va salonlarga qo'shamiz
avto1 = Avto('GM','Malibu','Qora',2010,20000)
avto2 = Avto('GM','Lacetti','Oq',2016,14000)
avto3 = Avto('GM','Damas','Qaymoq',2020,8000)
salon1.add_avto(avto1, avto2, avto3)

avto4 = Avto('Mazda', '6', 'Qizil', 2015, 34000)
avto5 = Avto('Wolkswagen', 'Polo', 'Qora', 2017, 30000)
avto6 = Avto('Honda', 'Accord', 'Oq', 2019, 45000)
salon2.add_avto(avto4, avto5, avto6)

car1 = Avto('Toyota','Carolla', 'Qora', 2020, 32000)
car2 = Avto('Tesla', 'Tesla', 'Qora', 2022, 50000)

#Obyektlarni chaqiramiz
salon1(car1, car2)#salon1 ga obyektlarni qo'shib yuboarmiz
#print(salon1())

#salonlarni qo'shamiz
salon3 = salon1 + salon2
print(salon3.name)#eski nomi
salon3.name = 'AvtoMax Lider'#salon3 nomini o'zgartiramiz
print(salon3.name)
print(salon3[:])

#yani talqinda
salon2 + car1#salon2 ga obyektni qo'shib yuboramiz
print(salon2())















