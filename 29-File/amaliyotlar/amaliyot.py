"""
SUSAMBIL



"""

while True:
    kino = input("Yaxshi ko'rgan kinoyigiz nomini kiriting(tugatish uchun 2marta entrni bosing):")
    if not kino:break
    with open('kino.txt', 'a') as file:
        file.write(kino +'\n')
  