import unittest
from shaxs_talaba_klassi import Shaxs

class ShaxsTest(unittest.TestCase):
    '''Shaxs nomli klassni tekshiradi'''
    def setUp(self):
        ism = 'Olim'
        familya = 'Olimov'
        passport = 'AA2345678'
        tyil = 1997
        #obyekt yaratildi
        self.shaxs1 = Shaxs(ism, familya, passport, tyil)

    def test_create(self):
        #Shaxs klasini hususiyatlarin itekshiramiz
        # assertIsNotNone() qiymat mavjutligini telshiradi
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)

    #Shaxs klasining metodlarini tekshiramiz
    def test_get_info(self):
        shaxs_info = "Olim Olimov.Passport:AA2345678, 1997-yilda tug'ulgan"

    def test_get_age(self):
        pass











unittest.main()

