'''
12 - and va or operatori
'''
# OR operatori foydalanish
#or-(yoki) ikki va undan ortiq shartlarni biri bajarilishini tekshirishda ishlatiladi!!!!!!
kun = input("Bugun kin nima?»")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
	print("Bugun dam olish kuni!")
else:
	print("Bugun ish kuni!")
#»»»»»»»
print(True or False)
print(True or True)
print(False or False)

#AND operatori
#and-(va) ikki va undan ortiq shartlarni barchasini tekshirishda ishlatiladi.Agar shertdan biri bajarilmasa False qiymatini qaytaradi
kun = input("Bugun kun nima:?")
harorat = float(input("Havo harorati qanday?:"))
if kun.lower()=='yakshanba' and harorat>=30:
	print("Bugun chumilishga boramiz!")
elif kun.lower()=='yakshanba' and harorat < 30:
    print("Uyda qoling!")
#»»»
#Bir nechta shartlarni aralashtirib yozish
yosh = int(input("Yoshingizni kiriting»"))
kun = input("Bugungi kun»")
if (yosh<7 or yosh>65) and kun=="chorshanba":
    print("Bugun siz uchun muzeyga kirish bepul")
#Boolean malumotlar turi
narx = 15000 #15000 minglik ovqat oldi
choy = True #mijoz choy oldi 
salat = False #mijoz salat olmadi
if choy and salat: #choy va salat olgan bo'lsa'
	narx = narx + 10000#Ming qo'shamiz'
elif choy or salat: #choy yoki salat olgan bo'lsa
    narx = narx + 5000#ming qo'shamiz
print(f"Jami {narx}so'm ")
	
#Bir nechta shartlarni ketma ketligini tekshirish
narx = 15000#mijoz 15 minga ovqat oldi
choy = 1#oldi
salat = 0#olmadi
non = 1#oldi
kompot = 1#olmadi
asarti = 0#olmadi
if choy: #agar choy olsa
      print("Mijoz choy oldi")
      narx = narx + 3000#ming qoshamiz
if salat: #agar salat olsa
      print("salat oldi")
      narx = narx + 5000#ming qoshamiz
if non: #agar non olsa
      print("non oldi")
      narx = narx +2000#ming qoshamiz
if kompot: #agar kompot olsa
      print("kompot oldi")
      narx = narx +1000#ming qoshamiz
if asarti:#agar asarti olsa
      print("asartiment oldi")
      narx = narx + 5000#ming qoshamiz

print("Jami", narx, 'so\'m')











