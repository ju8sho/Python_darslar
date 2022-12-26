"""
SUSAMBIL: author: Guni

**kwargs (**keyword arguments)

"""

def avto_info(kompaniya,model,**malumotlar):
    '''Avto haqidagi malumotlarni lug'at shaklida qaytaradi'''
    malumotlar['kompaniya']= kompaniya
    malumotlar['model']= model
    return malumotlar
avto1= avto_info('GM','Jip',rang='qora',yil='2022',karaobka='avto')
avto2= avto_info('Kia','K5',rang='qizil',narx='23000')
print(avto1,avto2)