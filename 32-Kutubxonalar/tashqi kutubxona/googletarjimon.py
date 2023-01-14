from googletrans import Translator

translator = Translator()#klassdan obyekt yaratamiz

msg = "\nTarjima uchun so'z kiriting:\nchiqib ketish uchun ext deb yozing!"

while True:
    text = input(msg)
    if text == 'ext':
        break
    else:
        tarjima = translator.translate(text, src='uz', dest='en')
        print(tarjima.text)
