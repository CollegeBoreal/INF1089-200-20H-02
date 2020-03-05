# https://www.youtube.com/watch?time_continue=1&v=24DWw6Ozkvo

from itertools import count, takewhile
def primes():
   def sieve(numbers):
       head = next(numbers)
       yield head
       yield from sieve(n for n in numbers if n % head)
   return sieve(count(2))

print(list(takewhile(lambda x: x < 60, primes())))
