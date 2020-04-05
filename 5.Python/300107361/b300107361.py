# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:56:16 2020

@author: Tochgaly-K.J.Etienne
"""

from itertools import count, takewhile 

def primes():
    def sieve(numbers):
        head = next(numbers)
        yield head
        yield from sieve(n for n in numbers if n % head)
    return sieve (count(2))



list(takewhile(lambda x: x < 60, primes())) 