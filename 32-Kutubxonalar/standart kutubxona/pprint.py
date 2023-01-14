# pprint() Chiroyli print

from pprint import pprint
import json

# file ni ochib olamiz
filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

# print(bemor)    
# pprint(bemor)

fayl = 'sample4.json'
with open(fayl) as file:
    sample = json.load(file)

pprint(sample)
