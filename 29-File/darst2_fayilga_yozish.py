"""
SUSAMBIL

File yaratish va file ga malumotlar joylash yozish

"""
##talablar txt ni shakilantiradi
# with open('talabalar.txt', 'w') as file:
#     file.write('murot alimov\n')
#     file.write('rustam goipov\n') 
#     file.write('abdulla hasanob\n')


##shaxsning malumotlarini  shakilantiradi
# filename = 'shaxs_malumot.txt'
# ism = 'Bobur Otajonov'
# tyil = 1997
# with  open(filename, 'w') as file:
#     file.write(ism + '\n')
#     file.write(str(tyil) + '\n')

#Yaratilgan file ga yana ma'lumot qo'shish
filename = 'shaxs_malumot.txt'
with open(filename, 'a') as file:#  a argumenti  buyerda append manosini beradi va ishlatiladi
    file.write('Temur Toshpulatov\n')
    file.write('2000')

