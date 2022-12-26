"""
SUSAMBIL

O'zgaruvchilarni file larda saqlash

"""

#Pickle file ga yozish bu file da pitondan tashqarida o'qib bo'lmaydi
#pickle  modulni chaqiramiz
import pickle #pikl o'qilishi

talaba1 = {'ism':'hasan', 'familya':'hasanov', 'tyil':2002, 'kurs':2}
talaba2 = {'ism':'olim', 'familya':'olimov', 'tyil':1995, 'kurs':4}

with open('info_pkl', 'wb') as file:#write binariy
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)
