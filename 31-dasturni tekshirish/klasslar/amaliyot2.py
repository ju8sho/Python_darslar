from shaxs_talaba_klassi import Talaba
import unittest

class TalabaTest(unittest.TestCase):
    '''Talaba klassini tekshiradi'''
    def setUp(self):
        ism = 'Olim'
        familya = 'Olimov'
        passport = 'AA2345678'
        tyil = 1997
        aydi = 1234567
        #obyekt yaratamiz
        self.talaba1 = Talaba(ism, familya, passport, tyil, aydi)

        