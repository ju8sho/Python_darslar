# setUp() metodidan foydalanish

#kerakli modullarni chaqirib olamiz
import unittest
from dars1 import Car

class CarTest(unittest.TestCase):
    '''Car klasini test qiladi setUp() metodidan foydalanilgan'''

    def setUp(self):
        make = "GM"
        model = "Malibu"
        year = 2022
        self.price = 40000
        self.km = 500
        self.avto1 = Car(make, model, year)
        self.avto2 = Car(make, model, year, price=self.price)

    #Car degan klassning hususiyatlarni tekshirish
    def test_create(self):
        #qiymat mavjutligini tekshirish uchun
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)

        #qiymat mavjut emasligini tekshirish uchun
        self.assertIsNone(self.avto1.price)

        #qiymat tengligini tekshitish uchun
        self.assertEqual(0, self.avto1.get_km())
        self.assertEqual(self.price, self.avto2.price)


    #Car degan klassning Metodlarni tekshirish
    def test_set_price(self):
        new_price = 45000 #yangi narx berdik
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)

    def test_add_km(self):
        #musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())

        #km ga km ni qo'shilishini tekshirish
        self.avto1.add_km(100)
        self.assertEqual(600, self.avto1.get_km())

        #manfiy qiymat kiritamiz
        new_km = -100
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)


    def test_get_info(self):
        avto1_info = 'GM Malubi, 2022-yil, 0km yurgan'

        #avto1 ni narxini va km ni o'zgartiramiz
        self.avto1.set_price(45000)
        self.avto1.add_km(700)

        avto1_info = 'GM Malubi, 2022-yil, 700km yurgan.Narxi 45000'

unittest.main()



