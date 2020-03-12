# Sieve

from itertools import count, takewhile

def primers():
  def sieve(numbers)
      head = next(numbers)
      yield head 
      yield from sieve(n for n numbers if n % head)
  return sieve(count(2))

#list(takewhile(lambda x: x < 40, primes() ))


