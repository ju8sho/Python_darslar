"""
SUSAMBIL: author: Guni



"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"{ism.title()}ning bahosini kiriting:")
        baholar[ism] = baho
        #[ism]kalit = baho qiymat bo'ldi
    return baholar
talabalar = ['ali','vali','hasan','husan']
baholar = bahola(talabalar[:])#ro'yxatdan nusxa olamiz
print(baholar)

