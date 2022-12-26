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
avto1 = Avto('GM','Malibu','Qora',2010,20000)
avto2 = Avto('GM','Lacetti','Oq',2016,14000)
print(avto1)
#Obyektlarni taqqoslash
print(avto1>avto2)

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

    def add_avto(self,avto):
        if isinstance(avto, Avto):
            self.avtolar.append(avto)
        else:
            print("Avto obyektini kiriting")


salon1 = AvtoSalon('MaxAvto')
print(salon1)
avto1 = Avto('GM','Malibu','Qora',2010,20000)
avto2 = Avto('GM','Lacetti','Oq',2016,14000)
avto3 = Avto('GM','Damas','Qaymoq',2020,8000)
#yuqoridagi obyektlarni salon 1ga qo'shamiz
for avto in [avto1, avto2, avto3]:
    salon1.add_avto(avto)
print(len(salon1))#salonimizda 3ta mashina bor
#Obyekt elementlariga murojat etish
salon1[0]
print(salon1[:])

#obyekt elementlarini o'zgartirish
avto4 = Avto('Mazda', '6', 'Qizil', 2015, 34000)
salon1[0] = avto4
print(salon1[0])




