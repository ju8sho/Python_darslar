'''

'''
#lists yaratish
mevalar = ['Olma', 'behi','nok','anor','banan']
narhlar = [1200,14.500,2000,1000,3000]
sonlar = ['bir','ikki',3,4,5,67,-8,56,89,-45,67,23,456,-234]#aralash ro'yhat
ismlar = []#bo'sh ro'yhat
#indeks orqali murojat qilish
print("1-meva: ",mevalar[0])
print("2-meva: ",mevalar[1])
#string metodlari
print("3-meva: ",mevalar[2].title())
print("4-meva: ",mevalar[3].upper())
#arifmetik amallar 
print(narhlar[3] + narhlar[4])
print(sonlar[-1])#eng oxirgi elementini bilish
#>>>
#elementlarni o'zgartirish
narhlar = [1200,14.500,2000,1000,3000]
narhlar[0] = 1500
narhlar[2] = narhlar[2] + 500
print(narhlar)
#>>>
#element qo'shish
mevalar.append("tarvuz")
#>>>
cars = []
cars.append("Nexia")
cars.append('Damas')
cars.append("Labo")
cars.append("Malubi")
#bo'sh ro'yhat to'ldi>>>>
cars = ['Nexia', 'Damas', 'Labo', 'Malubi']
#royhatni istalgan joyiga elemen qo'shish
cars.insert(0, "Tico")
cars.insert(2, "Kia")
#elentni o'cirish
del mevalar[1]
#qiymati bo'yicha 1 yoki kop birxil qiymatlarni o'chirish
mevalar.remove("nok")
cars.append('kia')
cars.remove('kia')
#elementlarni sug'urib olish
bozorlik = ["yog'",'un','piyoz',"go'sh","olma" ]
oldim = bozorlik.pop(4)
print("Men " + oldim.title() + " sotib oldim")
print("Sotib olinmagan mahsulotlar:",bozorlik," qoldi!.")
#pop()metodida indeks bermsa toyhatdan oxrgai elemaentni sug'uradi
print(bozorlik)
ol = bozorlik.pop()
print(bozorlik)