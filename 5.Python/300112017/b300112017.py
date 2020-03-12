# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:35:00 2020

@author: Ador
"""

from iterttools import count, takewhile

def primes():
    def sieve(numbers):
        head = next(numbers)
        yield head
        yield from sieve(n for n in numbers if n % head)
        return sieve(count(2))
