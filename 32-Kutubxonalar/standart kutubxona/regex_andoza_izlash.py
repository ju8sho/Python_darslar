# RegEx -Andoza yordamida matin izlash
import re 

word1 ='темир'
word2 = 'томир'
word3 = 'тулпор'

andoza = "^т...р$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

# misollar email ajratib olish
matin = """MohirDev.uz onlayn ta'lim platformasining rasmiy Telegram kanali gabarjubar34@gmail.com
Bu sahifamizda platformaga oid yangiliklar va foydali maqolalar qo'yib boriladi"""

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza, matin)
print(email)

# kuchli parolni tekshirish
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'

msg = "Yangi parol kiriting [( e.g. 123,@#$% )] simvollardan foydalaning:"

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Qabul qilindi")
        break
    else:
        print("qabul qiinmadi, mahfiy so'z kuchsiz!")