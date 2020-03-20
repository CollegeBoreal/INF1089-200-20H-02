import sys; sys.path.append('.') # Rajouter le repertoire courant
from b300107361 import primes
test = list(takewhile(lambda x: x < 60, primes())) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59] 
if  test:
     print('--------------------')
     print(':tada: :tada: :tada:')
else:
     print('--------------------')
     print(':no_entry: :no_entry: :interrobang:')
