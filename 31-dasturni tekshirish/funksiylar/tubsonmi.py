"""
SUSAMBIL



"""

# Mantiqiy qiymatlar

def tubSonmi(n):
    '''kiritilgan sonni tub, tub emasmi'''
    if n == 2 or n == 3:return True
    if n % 2 == 0 or n < 2: return False
    for a in range(3, int(n ** 0.5) + 1, 2):
        if n % a == 0:
            return False
    return True

#print(tubsnmi(2))