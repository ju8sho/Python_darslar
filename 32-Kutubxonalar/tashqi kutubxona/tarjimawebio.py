from googletrans import Translator
from pywebio.input import input, FLOAT
from pywebio.output import put_text

translator = Translator()#klassdan obyekt yaratamiz
def tarjimon():

    msg = "\nTarjima uchun so'z kiriting:\nchiqib ketish uchun ext deb yozing!"

    while True:
        text = input(msg)
        if text == 'ext':
            break
        else:
            tarjima = translator.translate(text, src='uz', dest='en')
            print(tarjima.text)
tarjimon()