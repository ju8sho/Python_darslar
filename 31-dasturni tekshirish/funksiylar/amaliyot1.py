"""
SUSAMBIL



"""

#uchta son qabu qilib ulardan eng kattasini qaytaradi
def maxson(son1, son2, son3):
    return max(son1, son2, son3)

#print(maxson(5,3,9))

#matinlardan iborat royxat qabul qilib ro'yxatdagi har bir matinni birinchi harifini katta harfga o'zgartiradi
def kattaHarf(royxat):
    for m in range(len(royxat)):
        royxat[m] = royxat[m].title()
        
# matn = ['ali','vali','aka','uka']
# kattaHarf(matn)
# print(matn)



        