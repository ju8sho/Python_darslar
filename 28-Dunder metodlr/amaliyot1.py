"""
SUSAMBIL

amaliyot dunder metdlar

"""

class Talaba:
    '''Talaba nomli class'''
    def __init__(self,ism,familya,tyil, passport, bosqich):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        self.bosqich = bosqich
        self.passport = passport
    def __repr__(self):
        return f"{self.ism} {self.familya} {self.bosqich}-bosqich talabasi"
        
    #Taqoslash metodlari    
    def __le__(self,parametr):
        '''Katta yoki teng '''
        return self.bosqich <= parametr.bosqich
    
    def __lt__(self,parametr):
        '''Kichik yoki katta'''
        return self.bosqich < parametr.bosqich
    
    def __eq__(self, parametr):
        '''Tengmi yoki teng emas'''
        return self.bosqich == parametr.bosqich
        
    #Malumot metodlari
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
    
    def get_info(self):
        return f"{self.ism} {self.familya} {self.tyil}-yilda tug'ulgan hozirda {self.bosqich}-talabasi"
    
    def set_bosqich(self,bosqich):
        '''Talabani kursini yanglovchi metod'''
        self.bosqich = bosqich    

    def tanishtir(self):
        '''Talabaning malumotlari'''
        return f"Ismim {self.ism} {self.familya} {self.tyil}-da tug'ulganman"



    
class Fan():
    '''Fan nomli class. keyinchalik fanga nom beriladi'''
    def __init__(self,nomi):
        self.nomi = nomi#Fan nomi
        self.talabalar = []
        
    def __repr__(self):
        '''Obyekt xaqida ma'lumot'''
        return f"{self.nomi} fani"      
    
    
    def __getitem__(self,index):
        '''Obyekt elementlarini indexs orqali ko'rishi'''
        return self.talabalar[index]
    
    def __setitem__(self, index, volue):
        '''Obyekt elementlarini index orqali o'zgartirish'''
        if isinstance(volue, Talaba):
            self.talabalar[index] = volue
            
    def __len__(self):
        '''Obyekt elementlarini uzunligini qaytaradi'''
        return len(self.talabalar)

    # def __add__(self,parametr):
    #     '''Fanga talabalarni qo'shadi'''
    #     if isinstance(parametr, Fan):
    #         fan = Fan(f"{self.nomi} {parametr.nomi}")
    #         fan.talabalar = self.talabalar + parametr.talabalar
    #         return fan
    #     elif isinstance(parametr, Talaba):
    #         self.add_student(parametr)
            
    def __add__(self, param):
        if isinstance(param, Talaba):            
            self.add_student(param)
            
    def __sub__(self, x):
        if isinstance(x, Talaba):
            self.talabalar.remove(x)
            
    # def __sub__(self, passport):
    #     for talaba in self.talabalar:
    #         if passport in talaba:
                
    #             self.talabalar.remove(talaba)
            
            
            
            
    def __call__(self):
        return [talaba for talaba in self.talabalar]
    
    def __call__(self, *parametr):
        if parametr:
            for param in parametr:
                self.add_student(param)
        else:
            return [talaba for talaba in self.talabalar]


    def get_name(self):
        '''Fan nomi'''
        return self.nomi        

    def get_students(self):
        '''Fanimizga yozilgan talabalar malumotlari'''
        return [x.get_info() for x in self.talabalar] 
    
    def add_student(self,*parametr):
        '''Fanga talabalrni qo'shish'''
        for talaba in parametr:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)
                   

matem = Fan('Matematika')
fizika = Fan('Fizika')

talaba0 = Talaba('Husan', 'Husanov', 2000, "AA1234567", 2)    
talaba1 = Talaba('olim', 'olimov',1997, "XC3458796", 3)
talaba2 = Talaba('Vali', 'Valiyev',1995, "WE0984534", 2)
matem(talaba0, talaba1)
matem + talaba2
matem - "AA1234567"
print(f"{matem}:{matem()}")

talaba3 = Talaba('Hasan', 'Hasanov', 1998, "AS1458745", 1)   
talaba4 = Talaba('Hasan', 'Alimov', 1999, "DR4561234", 4)   
fizika(talaba3) 
fizika + talaba4
print(f"{fizika}:{fizika()}") 

print(matem.get_students()) 
 