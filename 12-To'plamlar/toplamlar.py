'''
author : Guni
To'plamlar
'''
# to'plam yaratish {} jingalak qavis
sonlar = {1,2,3,4,5,6,5,6,2,4}#elementlar ko'p marta kelsa ham to'plam ichida 1 tasini saqlaydi
print(sonlar)
isimlar = {'alijon','valijon','boqijon','guni',}
print(isimlar)
#misol
mevalar = ['olma','behi','olma','uzum','behi','uzum']
mevalar = set(mevalar)
print(mevalar)

#to'plamga element qo'shish
# .add() METODI yagona element qo'shis
mevalar1 = {'uzum', 'behi', 'olma'}
mevalar1.add('banana')
# .update() METODI bir nechta element qo'shish
mevalar1.update(['anaor','qovun','tarvuz','ananas'])
print(mevalar1)
#To'plamarni ro'yxatga o'tikizish list()funksiyasi yordamida
mevalar = list(mevalar)
print(mevalar)

#Ro'yxtlarni to'plamga aylantirish
mevalar = set(mevalar)
print(mevalar)

#To'plamlar elementini o'chirish
# .discard() metodi yordamida bu metod yo'q element o'chirilsa xato qaytarmaydi
mevalar1 = {'banana', 'anaor', 'ananas', 'olma', 'qovun', 'uzum', 'tarvuz', 'behi'}
mevalar1.discard('ananas')
# remov()metodi yordamida bu metod esa yo'q element o'cirilsa xato qytaradi
mevalar1.remove('qovun')
sonlar1 = {1,2,3,4,5,6}
sonlar1.discard(7)#xato qaytarmaydi

#sonlar1.remove(7)# KeyError: 7 xatosini qytaradi
#print(sonlar1)#xato qaytaradi

# sug'urib olish
sonlar1 = {1,2,3,4,5,6}
son = sonlar1.pop()
print(son)
print(sonlar1)

#To'plamlar ustida amallar
# ikki to'plamni birlashtirish | belgisi yordamida
A = {1,2,3,4,5}
B = {1,3,5,6,7,8,9,}

C = A|B
print(C)
# .union()metodi yordamida
D = A.union(B)
print(D)

# Bir xil elementlarni topish uchin
A = {1,2,3,4,5}
B = {1,3,5,6,7,8,9,}
print(A&B)# &OPERATORI yordamida

# .intersektion() METODI YORDAMIDA
print(A.intersection(B))

# Ikki to'plam farqini topish
#(-) OPERATORI YORDAMID
A = {1,2,3,4,5}
B = {1,3,5,6,7,8,9,}

print(A-B)# 2 bilan 4 A to'plamda bor B da yo'q

#.diferanse()METODI yordamida
print(B.difference(A))# B to'plamidagi elementlar A to'plamida yo'q

# Simmetrik farq A va B to'plamga kiradigan lekin bir vaqitda ikkala to'plamga kirmaydigan elementlar
# ^ OPERATORI yordamida
A = {1,2,3,4}
B = {3,4,5,6}
print(A^B)#ikkala to'plamda bor elementlar simmetrik farqga kirmaydi

# .symmetric_difference METODI yordamida
print(A.symmetric_difference(B))
