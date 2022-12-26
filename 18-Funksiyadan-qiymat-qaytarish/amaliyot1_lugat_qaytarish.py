"""
SUSAMBIL: author: Guni

Amaliyot

"""
def user_info(ism, familya, yosh, tyil, tjoy, emanzil='', tel=None):
    '''Malumot qabul qilib lug'atga joylaydi'''
    info = {
            'ism':ism,
            'yosh':yosh,
            'familya':familya,
            'tyil':tyil,
            'tjoy':tjoy,
            'emanzil':emanzil,
            'tel':tel,
            }
    return info

talaba1 = user_info('ali','valiyev',24,1997,'namangan','vali@examplay.com',+998901234567)
talaba2 = user_info('vali','valiyev',23,2002,'navoiy',)
print(talaba1,talaba2)

