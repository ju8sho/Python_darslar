"""
SUSAMBIL



"""
#Sonlarni tekshirish
import unittest
from circle import getAre, getPerimeter

class CircleTest(unittest.TestCase):
    def test_are(self):
        self.assertAlmostEqual(getAre(10), 314.159)
        self.assertAlmostEqual(getAre(3), 28.27431)
        
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)
        
unittest.main()