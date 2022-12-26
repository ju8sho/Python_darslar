
"""
     AMALIYOT -07
"""
#ismlar degan ro'yhat yarating va 3 ta ism kiriting 
ismlar = []
ismlar.append("Bobur") 
ismlar.append('olim')
ismlar.append('guni')
#ro'yhatdagi har bir isimga habar yozing konsolga chiqaring

print("Salom ",ismlar[0]," yahshimisan?")
print(ismlar[1].title()," bugun biznikiga kelgin!")
print("Men mushugimni ",ismlar[2]," deb nomladim!")
#sonlar degan ro'yhat yarating va turli hil sonlar yuklang
sonlar = ['bir','ikki',3,4,5,67,-8,56,89,-4.5,67,23,45.6,-234]
#arifmetik amallar bajarish va qiymatlarni o'zgartirish
print(sonlar[2] + sonlar[3])
sonlar[1] = 2
sonlar[0] = 1
print(sonlar)
sonlar.remove(-8)
del sonlar[-1]
print(sonlar)
sonlar[0] = sonlar[0]+1
sonlar[7] = sonlar[7]+1
print(sonlar)
#>>>>
#t_shaxislar va z_shaxislar degan 2 ta ro'yxat yarating
#va biriga o'zingiz yoqtirgan tarixiy shaxsni ,ikkinchisiga
#zamonimizdagi tirik shaxslarni kiriting
#yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib
#olib konsolga chiqaring
t_shaxslar = ["Imom Al Buhoriy","Al Termiziy","Al Xorazmiy"]
z_shaxslar = ["Ilon Mask","Robbert","Anvar Narzullayev"]
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\n\
zamonaviy shaxislardan {z_shaxslar.pop(2)} bilan\n\
suxbat qilishni istar edim!\n")
#>>>
#frendis degan bo'sh ro'yxat tuzing va unga .append()
#yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan
#do'slaringizni kiriting
friends = []
friends.append("Bobur")
friends.append('Olim')
friends.append("Aziz")
friends.append("G\'ani")
friends.append("Guni")
print(friends)
#Yuqoridagi ro'yxatdan mehmonga kelaolmaydigan
#odamlarni o'chirib tashlang
friends.remove("Aziz")
friends.remove("Bobur")
#Ro'yxatning oxriga,boshiga va o'rtasiga yangi
#ismlar qo'shing
friends.append("Vali")
friends.insert(2, "Salim")
friends.insert(3, "Halil")
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating 
#pop() va append() metodlari yordamida mehmonga kelgan
#do'slarni friends ro'yhatidan sug'urib mehmonlar
#ro'yxatiga qo'shing
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
print("\nKelgan mehmonlar:", mehmonlar)
