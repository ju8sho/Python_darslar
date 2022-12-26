"""
Created on Mon Sep 19 09:59:33 2022

@author: Guni

08 amaliyot
"""
#ozingizga ma'lum davatlar ro'yxatini tuzing va konsolga chiqaring
goroda = ['Rosiya','Qozog\'iston','qirg\'iziston','AQSH','Kanada','Avstralya']
print(goroda)
#ro'yxat uzunligini chiqaring
print("Ro'yxat uzunligai:",len(goroda))
#sorted()yordamida ro'yxatni tartiblang va chiqaring
print(sorted(goroda))
#sorted()yordamida teskari tartibda  chiqaring
print(sorted(goroda, reverse=True))
#asil ro'yxatni chiqaring
print(goroda)
#reverse()metodi yordamida ortidan boshlab chiqaring
goroda.reverse()
print(goroda)
#sort()metodi yordamida ro'yxatni alifbo bo'yicha tartiblang..
goroda.sort()
print(goroda)
#.keyin alfboga teskari tartibda chiqaring
goroda.sort(reverse=True)
print(goroda)
#120 dan 1200 gacha bo'lgan juft sonlar royxatini tuzing.
juft_sonlar = list(range(120,1200,2))
#ro'yxatdagi sonlar yigindisini xisoblang va chiqaring
jami = sum(juft_sonlar)#1-variant
print(sum(juft_sonlar))#2-variatnt
print("juft sonlar jami:",jami)
#ro'yxatdagi eng kata va kichik son o'rtasidagi ayirmani xisoblab chiqaring
#1-variant
katta = max(juft_sonlar)
kichik = min(juft_sonlar)#1
print(f"\nEng katta sonlar:{katta}\n\
eng kichik sonlar:{kichik}\n")
#2-variant
print("Sonlar o'rtasidagi ayirma:",katta - kichik)
#3-variant
print(max(juft_sonlar)-min(juft_sonlar))
#ro'yxatdagi elementlar sonini xisoblang
#1-variant
print("Ro'yxatdagi elementlar:",len(juft_sonlar), 'ta')
#2-variant
print(len(juft_sonlar))
#Royxatning boshidan,o'rtasidan va oxridan 20 qiymat chiqaring
print(juft_sonlar[:20])
print(juft_sonlar[-20:])
print(juft_sonlar[520:540])
#taomlar degan ro'yxat yarating 5 ta taom kiriting
taomlar = ['Sho\'rva','Shashlik','Osh','Makaron','non']
#nonushta degan yani royxatga taomlardan nusxa oling
nonushta = taomlar[:]
#yangi royxatda faqat nonushtaga yeyiladigan taomlarni qoldiring
#va unga yana 2 ta taom qo'shing
del nonushta[0:4]
nonushta.append('Asal')
nonushta.append('Saryog\'')
#ikkala ro'yxatni ham konsolga chiqaring
print("Taomlar:",taomlar)
print("Nonushta:",nonushta)
#yuqoridagi nonushta royxatni ozgarmas ro'yxatga aylantiring
##va nonushta[0] = 'qymoq' va 'sut' deb qiymat bering
nonushta = tuple(nonushta)
nonushta[0] = 'qaymog\''
nonushta[1] = 'bo\'lka'
print(nonushta)
#natija..
#'tuple' object does not support item assignment

