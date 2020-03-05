# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:57:47 2020

@author: dell
"""


#imprimer de 0 a 9

range (10)
a = [ x for x in range (10)]

print (a)

#imprimer les nombres pairs

b = [x *2 for x in range (10)]

print (b)

# imprimer les nombres impairs

c = [x for x in range (10) if x % 2 != 0 ]

print (c)

# methode 2 pour imprimer les nombres pairs

d = [x for x in range (10) if x % 2 == 0]

print (d)

# set
a = {2,2,2,2,}

print (a)

a = {3, 3,  2, 2, 2}
print (a)

b = {'a' : 3, 'b': 4, 'c': 5}
print (b)

a, b, c = (8, 6, 10)
print (a,b,c)

x, y, z = (1, 1/2, 0.2)
print (x, y, z)

a, b, c = (8, 6, 10)

