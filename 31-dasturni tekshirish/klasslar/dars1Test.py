#kerakli modullarni chaqirib olamiz

import unittest
from dars1 import Car

#hususiyatlarni  tekshirish
class CarTest(unittest.TestCase):
    '''Car klasini tekshiruvchi test'''
    def test_create(self):
        #obyekt yaratib ko'ramiz
        avto1 = Car('toyota', 'camry', 2020)

        #assertIsNotNone() qiymat mavjutligini telshiradi
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)

        #assertIsNone() qiymat mavjut emasligini tekshiradi
        self.assertIsNone(avto1.price)

        #assertEqual() qiymat tenglikni tekshiradi
        self.assertEqual(0, avto1.get_km())

        #yangi obyekt yaratib narxini ham ko'rsatamiz
        avto2 = Car("toyota", 'camry', 2022, price=45000)
        self.assertEqual(45000, avto2.price)

#testni ishlatib ko'ramiz
unittest.main()