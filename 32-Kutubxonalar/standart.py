"""
SUSAMBIL



"""

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

