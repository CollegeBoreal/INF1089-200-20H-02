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