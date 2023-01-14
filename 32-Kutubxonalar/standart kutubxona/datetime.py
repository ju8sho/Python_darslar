

import datetime as sana

#hozirgi vaqtni ko'rish
hozir = sana.datetime.now()
print(hozir)

#sanani ajratib olish
print(hozir.date())

#vaqtni ajratib olish
print(hozir.time())

#saotni ajratib olish
print(hozir.hour)

#minutni ajratib olish
print(hozir.minute)

#sekuntni ajratib olish
print(hozir.second)

#bugungi sana
bugun = sana.date.today()
print(f"Bugun sana:{bugun}")

#sanani qo'lda kiritish
ertaga = sana.date(2022, 12, 30)
print(f"Ertaga sana:{ertaga}")

# Faqat vaqit bilarn ishlash uchun  .datetime.now().time() metotiga murojat qilinadi
hozir = sana.datetime.now()
vaqithozir = hozir.time()
print(f"Hozir soat:{vaqithozir}")

#time() metodiga istalgan vaqitni  qo'lda berishimiz mumkin
vaqtKeyin = sana.time(12, 3, 00)
print(vaqtKeyin)

#Ayitish operatori yordamida 
today = sana.date.today()
ramazon = sana.date(2023, 3, 13)
farq = ramazon-bugun
print(f"Ramazonga {farq.days} kun qoldi")

# Sanani uzimizga moslab chiqarish
vaqit = hozir.strftime("%H:%M:%S")
print(f"Hozir soat:{vaqit}")

#Kun oy yil
sana = hozir.strftime("%d-%m-%y")
print(f"Bugun sana:{sana}")

# Kun oy yil va sana
sana_vaqit = hozir.strftime("%d/%m/%y, %H:%M")
print(sana_vaqit)
