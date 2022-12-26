'''
    MATIN (STRING)
'''
viloyat = "Farg'ona"
avto = 'cobalt'
matn = 'man yangi ℡ nomer oldim'
print(matn)
# Matin ustida amallar
ism = 'Guni'
print("Mani ismim " + ism)
ism = 'Guni'
sharif = "Mushukboyevich"
print(ism +' '+ sharif)
#
ism_sharif = f"{ism} {sharif}"
print(ism_sharif)
#
fname = 'Mushukboyevich'
iname = "Guni"
matn = f"Salom mani ismim {iname}.{iname} {fname}!"
print(matn)
#
tyil = 1997
print(f"Siz {tyil}-yilda tug\'ilgansiz")
print(f"Yoshingiz {2022 - tyil}da")
# mahsus belgilar \t, \n
print("Salom \tDunyo")# bo'sh joy tashlash
print("Vsem \nprivet")# qator tashlash
# Matinlar b\n ishlash upper.(),lover.()
ism = 'Guni'
sharif = "Mushukboyevich"
ism_sharif = f"{ism} {sharif}"
print(ism_sharif.lower())# bosh hariflar kichik bo'ldi
print(ism_sharif.upper())# barcha hariflar katta bo'ldi
# .title(), .capitalize()
ism_sharif = "guni mushukboyevich"
print(ism_sharif.title())# so'zning 1chi  hariflari katta bo'ldi
print(ism_sharif.capitalize())# 1chi so'zning 1chi  harifi katta bo'ldi
#
print("guni mushukboyevich".upper())
#
#.strip(),.rstrip(),.lstrip() 
meva = '  olma    '
print("Man " + meva.lstrip()+ "yahshi ko\'raman")# matin boshidan bo'shliq oladi
print("Man " + meva.rstrip()+ "yahshi ko\'raman")# matin ohridan bo'shliq oladi
print("Man " + meva.strip()+ "yahshi ko\'raman") # matin boshidan va ohridan bo'shliq oladi 
# aslini olish
meva = '  olma    '
print("Man " + meva + "yahshi ko\'raman")
meva = meva.strip()#metod o'zgaruvchi qiymatiga yuklandi
print("Man " + meva + " yahshi ko\'raman")
#
# .input() FUNKSIYASI
ism = input("Ismingiz nima?")
print("Zdrastvuyte, " + ism)


