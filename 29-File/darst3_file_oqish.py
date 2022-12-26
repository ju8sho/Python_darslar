"""
SUSAMBIL

File larni ochib uning elementlarini, ma'lumotlarini o'qish

"""
#file larni qatorma qator o'qish
filename = 'data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)
        
#file larni ro'yxatga joylash
with open(filename) as file:
    talabalar = file.readlines()#readlines() metodi file ichidagi elementlarni qatorma qator chiqaradi
print(talabalar)

#ro'yxat ichidagielementlarni ozalash
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)         