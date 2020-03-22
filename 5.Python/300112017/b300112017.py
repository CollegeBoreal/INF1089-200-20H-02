# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:35:00 2020

@author: Ador
"""

from itertools import count, takewhile

def primes():
    def sieve(numbers):
        head = next(numbers)
        yield head
        yield from sieve(n for n in numbers if n % head)
        return sieve(count(2))
     
list(takewhile(lambda x: x < 30, primes()))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
