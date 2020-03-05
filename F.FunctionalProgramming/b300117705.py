# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:01:47 2020

@author: acorl
"""


a = [x for x in range (10)]
print(a)

s = [2*x for x in range(10)]
print(s)

j = [x for x in range(10) if x % 2 == 0]
print(j)

g =  [x for x in range(10) if x % 2 != 0 ]

# set
a = {2,2,2,2}

print(a)

a = {3, 3, 2, 2, 2}
print (a)

b = {'a' : 3, 'b': 4, 'c' : 5}
print (b)

a, b, c = (8, 6 , 10)
print (a,b,c)


x, y, z = (1, 1/2, 0.2)
print (x, y, z)

a, b, c = (8, 6, 10)