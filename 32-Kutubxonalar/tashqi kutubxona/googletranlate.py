from googletrans import Translator

translator = Translator() # translator bu obyekt = Translator() esa klass

matin = "Python - dunyodagi eng mashxur til hisoblanadi"

natija = translator.translate(matin)
print(natija.text)

# Boshqa tillarga tarjima qilish
tarjima_ru = translator.translate(matin, dest='ru')
print(tarjima_ru.text)

tarjima_uz = translator.translate(matin, dest='uz')
print(tarjima_uz.text)

matin_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = translator.translate(matin_en, dest='uz')
print(tarjima_uz.text)
# Matin tilin ham alohida ko'rsatish  src=' ' parametri orqali
tarjima_uz = translator.translate(matin_en, src='en', dest='uz')
