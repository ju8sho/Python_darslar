"""
SUSAMBIL



"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
#metod:
    def test_toliq_ism(self):
        '''To'liq ismli metod'''
        formated_name = get_full_name('alijon', 'valiyev')
        self.assertEqual(formated_name, 'Alijon Valiyev')
    
#metod: otasi uchun metod yaratildi
    def test_toliq_ism_otasi(self):
        name = get_full_name('hasan', 'husanov', 'olimovich')
        self.assertEqual(name, 'Hasan Olimovich Husanov' )
        
    
#o'qitib ko'ramiz        
unittest.main()