"""
SUSAMBIL: author: Guni

Amaliyot

"""

def aylana_info(radius,pi=3.14159):
    '''radius,diametr,parametr,yuza ni qaytaradi'''
    aylana = {'radius':radius,
              'diametr':2*radius,
              'parametr':2*radius*pi,
              'yuza':pi*radius**2}
    return aylana
son = aylana_info(2)
print(son)