"""
SUSAMBIL: author: Guni



"""
talabalar = ['ali','vali','hasan','husan']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"{ism.title()}ning bahosini kiriting:")
        baholar[ism] = baho
        #[ism]kalit = baho qiymat bo'ldi
    return baholar

baholar = bahola(talabalar)#ro'yxatdan nusxa olamiz
print(baholar)
print(talabalar)