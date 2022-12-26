"""
SUSAMBIL

Amaliyot

"""
import json

data = {'Model':'Malibu', 'Rang':'Qora', 'Yil':2020, 'Narx':23000}
data_json = json.dumps(data, indent=4)
#datani json fayilga kiriting
with open('data.json', 'w') as f:
    json.dump(data, f)
    
    
talaba_json = """{"ism":"Hasan", "familya":"Hasanov", "tyil":1997}""" 

talaba = json.loads(talaba_json)

print(f"{talaba['ism']} {talaba['familya']}") 

#student json fayilidan ism va familya fakultetini chiqaring 
with open('talaba.json', 'w') as f:
    json.dump(talaba, f)
    
with open('students.json') as f:
    data = json.load(f)

for item in data['student']:
    print(f"{item['name']} {item['lastname']}"
          f"Faculty of:{item['faculty']}") 
    
# wiki json fayilidan malumot chiqaramiz
with open('api-result.json') as f:
    wiki = json.load(f)
print(wiki['query']['pages']['13801']['title'])
print(wiki['query']['pages']['13801']['extract'])
    
    
    
    
    
    