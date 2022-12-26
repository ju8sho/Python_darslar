"""
SUSAMBIL: author: Guni

Amaliyot1

"""

#Foydalanuvchina ismini va yoshini so'rab uning tug'ulgan yilini hisoblaydigan funksiya
def ism_yosh_sorab(ism,yosh,tyil=2022):
    '''Foydalanuvchina ismini va yoshini so'rab uning tug'ulgan yilini hisoblaydigan funksiya'''
    print(f"Hurmatli {ism.title()} siz {tyil-yosh} yilda tugulgansiz")

user1 = input("ismingizni iriting:")
user2 = int(input("Yoshingizni kirinting:"))
ism_yosh_sorab(user1, user2)
