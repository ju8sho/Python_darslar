"""
SUSAMBIL



"""

with open('pi_milleon.txt') as pi:
    pi = pi.read()

pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = pi.replace(' ', '')
def pi_tyl(ty):
    ty = str(ty)
    if ty in pi:
        print("Bor ekan")
    else: print("Yo'q ekan")
    return ty
pi_tyl(25171971)
    