# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 04:35:38 2020

@author: Ador
"""

from itertools import count, takewhile

def primes():
  def sieve(numbers):
      head = next(numbers)
      yield head 
      yield from sieve(n for n in numbers if n % head)
  return sieve(count(2))

list(takewhile(lambda x: x < 60, primes()))