"""
SUSAMBIL

O'zgaruvchilarni file dan o'qish

"""

#modulni chaqiramiz
import pickle

with open('info_pkl', 'rb') as file:#read binary
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)