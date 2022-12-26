
"""
@author: Guni
"""
#ismlar degan ro'yxat yarating va kamida 3 ta yaqin
#do'stingizning ismini kiriting
ismlar = []
ismlar.append("Olim")
ismlar.append("Guni")
ismlar.append("Salim")
##Ro'yxatdagi har bir do'stingizga qisqa 
#xabar yozib konsolga chiqaring: 
ismlar = ['Olim', 'Guni', 'Salim']
print("Salom " +ismlar[0]+ " yahshimisan")
print(f"{ismlar[1]} bugun {ismlar[2]} keladi!")
#>>>>>
## sonlar deb nomlangan ro'yxat yarating va ichiga 
#turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [1, 9, -9, 9.3, +3,]
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar
#bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini
#o'zgartiring, ba'zilarini esa almashtiring.
sonlar[1] = sonlar[1] +1
sonlar[2] = 10
sonlar[4] = sonlar[4] -2
sonlar[3] =15
print(sonlar)
#>>>>>
#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga
#o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga
#esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
tshaxslar = ["Al Beruniy","Enshteyn"]
zshaxslar = ["Tonni","Bryus"]
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib
#olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f"\nBugun {tshaxslar.pop(0)} nomidagi muzeyga bordik\n\
keyin, {zshaxslar.pop(0)} kinosini ko'rdik")
#>>>>>
#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 
#ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
doslar = []
doslar.append("Ali")
doslar.append("Sardor")
doslar.append("Guni")
doslar.append("Salim")
doslar.append("G'ani")
#>>>>
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove()
#metodi yordamida o'chrib tashlang.
doslar.remove("Ali")
doslar.remove("G'ani")
##Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
doslar.append("Bobur")
doslar.insert(2, "Olim")
doslar.insert(0, "Halim")
print(doslar)
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va 
#.append() metodlari yordamida mehmonga kelgan do'stlaringizning
#ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga
#qo'shing.
mehmonlar = []
mehmonlar.append(doslar.pop(0))
mehmonlar.append(doslar.pop(2))
print("\nKelgan mehmonlar:",mehmonlar)