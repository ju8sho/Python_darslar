# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 19:57:39 2022

@author: guni
"""
# try:
#     x = int( input( "son kiriting: " ) )
#     y = int( input( "Yana bir son kiriting: " ) )
# except ValueError:
#     print("Butun son kiritmadingiz!")

# else:
#     print( x ,'/', y, '=',x/y)


while True:
    x = int(input( "son kiriting: " ))
    y = int(input( "Yana bir son kiriting: " ))
    c = x,y
    if c.isdigit():

        print("Son kiritmadingiz")
        break
print( x ,'/', y, '=',x/y)
