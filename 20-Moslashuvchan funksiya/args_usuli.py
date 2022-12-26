"""
SUSAMBIL: author: Guni

*args    (*arguments)

"""
# *args usuli
def summa(*sonlar):
    '''Kiritilgan sonlar yig'indisini qaytaradi'''
    yigindi= 0
    for son in sonlar:
        yigindi+= son
    return yigindi
#print(summa(1,4,5))

#argis usulida barcha kiritilgan parametirlar o'zgarmas ro'yxat bo'ladi (tuple)o'zgarmas ro'yxat
#Soddaroq qilib yozish ham mumkin
def natija(*sonlar):
    '''Kiritilgan sonlar yig'indisini qaytaradi'''
    return sum(sonlar)
#print(summa(1,4,5))


#Bir nechta argument qabul qilsa
def yigindi(a,b,*sonlar):# a va b majburiy qiymat bo'ldi undan keyin ixtiyoriy
    '''Kiritilgan sonlar yig'indisini qaytaradi'''
    return a+b+sum(sonlar)
print(yigindi(-10,10,2))









