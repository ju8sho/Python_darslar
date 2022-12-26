'''

'''

#foydalanuvchi kiritgn sonni kubini va kvadratini chiqar
print("Kvadrat va Kubni hisoblaydi!")
son = int(input("Son kiriting: "))
kvd = son**2
kbi = son**3
print("Kvadrati:",kvd ,"Kubi:",kbi)
#foydalanuvchidan yoshini so'rab tug'ulgan yilini hisoblash
yosh = int(input("yoshingizni kiriting: "))
javb = 2022 - yosh
print("Siz ", + javb,"yilda tug\'ulgansiz" )
#foydalanuvchi 2 son kirit ularnidan arifmetik amallar bajarilsin
son1 = int(input("a-Son kiriting: "))
son2 = int(input("b-son kiriting: "))
a,b,s,d = son1+son2,son1*son2,son1/son2,son1-son2
print("a+b=",a, "a*b=", b, "a/b=",s, "a-b=",d )