"""
SUSAMBIL



"""
#Mantiqiy qiymatlarni tekshirish
import unittest
from tubsonmi import tubSonmi

class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
        
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(256))
        self.assertFalse(tubSonmi(489))
        
unittest.main()