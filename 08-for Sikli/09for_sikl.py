"""
Created on Mon Sep 19 20:27:49 2022
@author: Guni
for sikli
"""

mehmonlar = ['Halim', 'Sardor', 'Guni', 'Olim', 'Salim', 'Bobur']
for mehmon in mehmonlar:
    print(mehmon)
    
#>.
mehmonlar = ['Halim', 'Sardor', 'Guni', 'Olim', 'Salim', 'Bobur']    
for mehmon in mehmonlar:#sikl sharti
    print(f"Hurmatli mehmon:{mehmon},")
    print("Sizni 20-Sentyabr kuni naxorgi oshga taklif qilamiz")
    print("Hurmat bilan Palonchiyevlar oilasi")
    #sikl bandi
print("Dastur tugadi!")#sikl tashqarisidagi cod
cars = ['damas','nexia','labo']
for i in cars:#sikl sharti
    print(i.title())
print("Ko'rganlar qilar havas")    
#>.sonli ro'yxatlari bilan ishlash
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng!")
#>.
numbers = list(range(1,11))
numbers_kv = []
for number in numbers:
    numbers_kv.append(number**2)
print(numbers)
print(numbers_kv)  
#..
#for va input()
frends = []
print("5 ta yaqin do'stingiz kim?")
for i in range(5):
  frends.append(input(f"{i+1}-ismini kiriting :"))
print(frends)