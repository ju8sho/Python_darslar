'''
09 - elif amaliyot
'''
#Yangi cars degan ro'yxat tuzing va Ro'yxat elementlarini bosh harifini katta harfda konsolga chiqaring "GM" uchun ikkala harfni katta qilib chiqaring
yangi_cars = ["tayoto",'mazda','hyundai','gm','kia']
for cars in yangi_cars:
	if cars =='gm':
		print(cars.upper())
	else:
		print(cars.title())
#yuqoridagi kodni teng emasmi(!=)operatori yordamida ham bajarib ko'ring
yangi_cars = ["tayoto",'mazda','hyundai','gm','kia']
for cars in yangi_cars:
	if cars !='gm':
		print(cars.title())
	else:
		print(cars.upper())		
		
#Foydalanuvchidan login ism so'rang agar foydalanuvchi admin bolsa Hush kelibsiz admin! foydalanuvchilar ro'yhatini ko'rasizmi? degan habarni konsolga chiqaring agar foydalanuvhi bo'lsa hush kelibsiz foydalanuvchi login ismi chiqaring konsolga.
login = input("Login ism kiriting:")
if login == 'admin':
		print("Hush kelibsiz Admin!. Foydalanuvchilar ro'yxatini ko'rasizmi?:")		
else:
		print("Hush kelibsiz",login)
#Foydalanuvchidan 2ta son kiritishini so'rang agar sonlar bir biriga teng bo'lsa Sonlar teng ekan degan xabar chiqaring
print("2ta son kiriting")
a = input("a-son kiriting:")
b = input("b-son kiriting:")
if a == b:
		print("Sonlar teng ekan")	
else:
		print("Sonlar teng emas")	
		
#Foydalanuvchidan istalgan son kiritishini so'rang agar son musbat bo'lsa uni ildizini hisoblab konsolga chiqaring aks holda manfiy bolsa musbat son kiriting degan xabar chiqaring
son = int(input("Son kiriting:"))
if son >0:
		print(f"{son}-ning ildizi:{son**2}")
else:
		print("Musbat son kiriting")
#kiritilgan soni toq yoki juft ekanligini aniqlovchi kod yozing
son1 = int(input("Son kiriting:"))
for s in range(son1,2):
		if s !=son1:
		    print("Juft son")	
else:
	print("Toq son")		    		