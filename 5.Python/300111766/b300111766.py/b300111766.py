# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:44:02 2020

@author: CHEIKH
"""



from itertools import count, takewhile

def primes():
  def sieve(numbers):
      head = next(numbers)
      yield head 
      yield from sieve(n for n in numbers if n % head)
  return sieve(count(2))

list(takewhile(lambda x: x < 50, primes()))

# Booleans True or False
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


a = 2
b = 3
c = 5
print( a == b)
print( a+b == c)
print( a < b )
print( a <= c)
print( type( a == c) )

a = 6
b = 7
c = 42
print(1, a == 6)
print(2, a == 7)
print(3, a == 6 and b == 7)
print(4, a == 7 and b == 7)
print(5, not a == 7 and b == 7)
print(6, a == 7 or b == 7)
print(7, a == 7 or b == 6)
print(8, not (a == 7 and b == 6))
print(9, not a == 7 and b == 6)

# Python lists

thislist = ["apple", "banana", "cherry"]
print(thislist)



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

maListeDeMeubles = ['table','chaise','frigo']
maListeDeMeubles.sort()  #Tri de la liste
for unMeuble in maListeDeMeubles:
   print('longueur de la chaîne ', unMeuble, '=', len(unMeuble))
   
   thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])