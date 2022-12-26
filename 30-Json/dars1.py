"""
SUSAMBIL

Json 

"""

import json

x = 10
x_json = json.dumps(x)

ism = 'Anvar'
ism_json = json.dumps(ism)

sonlar = [12,34,56,7,8]
sonlar_json = json.dumps(sonlar)


bemor = {
    "ism":"Alijon Valiyev",
    "yosh":25,
    "oila":True,
    "farzandlar":("Ahmad", "Bonu"),
    "allergiya":None,
    "dorilar":[
        {"nomi":"Analgin", "miqdori":0.5},
        {"nomi":"Panadol", "miqdori":1.2}
        ]
    }

    
#bemor_json = json.dumps(bemor)
#tushunarli holda chiqarish
bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)

#json formatdagi matinni python formatga o'tkazadi  loads() funksiyasi
bemor = json.loads(bemor_json)
print(bemor)

with open('bemor.json', 'w')as f:
    file = json.dumps(bemor)
    json.dump(file, f)
    
with open('bemor.json') as f:
    bemor = json.load(f)
    
print(type(bemor))
print(bemor)

#json fayillar tarkibidan pythonga yuklab olish. load()funksiyasi








