import math

#pi qiymati
PI = math.pi
print(f'Pining qiymati:{PI}')

# e natural logarifm asosi
E = math.e
print(f"e ning qiymati:{E}")

# Trigonometrya funksiyalar
a = math.sin(math.pi/2)
b = math.cos(0)
c = math.tan(PI)

# Burchakdan radianga, va aksincha,  konvertatsiyalar qilish
a1 = math.degrees(math.pi/2)
b1 = math.radians(90)

# Logarifmlar
#natural logorifm
a2 = math.log(5)

#10 asosli logarifm
b2 = math.log10(100)

#Sonlarni yaxlitlash.  yaqinroq son chiqaradi
x =  4.6 
print(math.ceil(x))#bu son yuqori qismi 5 soniga yaqinroq
print(math.floor(x))#bu son quyi qismi 4 soniga yaqinroq

# Ildiz va Daraja
n = 81
#kvadrat ildizi
n1 = math.sqrt(n)

# Darajaga oshirish
n2 = math.pow(n,3)#n ning kubi
n3 = math.pow(n, 5)# n ning 5-darajasi
n3 = math.pow(125, 1/3)# 125 dan  kub ildizi

# # Kompleks sonlar bilan ishlash uchun cmath moduli ham bor!!!!