'''
11 - if -elif -else . Bir nechta shartlarni tekshirish
'''

son= int(input("Son kiriting:"))
if son>0:
	print("Son musbat")
elif son <0:
	print("Son manfiy")
else:
	print("Son 0 ga teng")
#»»»
yosh = int(input("Yoshingiz nechida?"))
if yosh<4:
	print('Sizga kirish bepul')
elif yosh<=12:
	print('Sizga kirish 5000 so\'m')
else:
	print("Sizga kirish 10000 so'm")
#»»print() operatorini qayta qayta yozmaslik usuli
yosh = int(input("Yoshingiz nechida?"))
if yosh <4:
	price = 0
elif yosh <=12:
	price = 5000
else:
	price = 10000
print(f"Sizga kirish {price} so'm") 	
#»»
#Kodni kelajakda o'zgartirish imkoni
yosh = int(input("Yoshingiz nechida?"))
if yosh <4:
	price = 0
elif yosh <=12:
	price = 5000
elif yosh < 65:#O'zgartirish kiritdik akisholda agar yosh kichik  bolsa 65 dan 10000 som
	price = 10000
elif yosh >=65:#else qismi majburiy emas!
	price = 8000	
print(f"Sizga kirish {price} so'm")
#»»»




