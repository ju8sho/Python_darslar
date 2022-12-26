"""
SUSAMBIL: author: Guni

Amaliyot

"""
def user_info(ism, familya, yosh, tyil, tjoy, email='', tel=None):
    '''Malumot qabul qilib lug'atga joylaydi'''
    info = {
            'ism':ism,
            'yosh':yosh,
            'familya':familya,
            'tyil':tyil,
            'tjoy':tjoy,
            'emanzil':email,
            'tel':tel,
            }
    return info


mijozlar = []
while True:
    print("\nMijozlar ro'yxatini kiriting\n",end='')
    ism = input("Ismi?:")
    familya= input("familyasi?:")
    yosh = int(input("yoshi?:"))
    tyil = int(input("tug'ulgan yili?:"))
    tjoy = input("turar joyi?:")
    email = input("elektiron manzili?:")
    tel = input("tel raqam?:")
    mijozlar.append(user_info(ism, familya, yosh,tyil,tjoy,email,tel))

    javob = input("Yana kiritasizmai?(yes/no):")
    if javob == 'yes':
        continue
    elif javob == 'no':
        break


print("Mijozlar ro'yxati:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familya'].title()} {mijoz['yosh']}-yoshda",
          f"tel:{mijoz['tel']}")