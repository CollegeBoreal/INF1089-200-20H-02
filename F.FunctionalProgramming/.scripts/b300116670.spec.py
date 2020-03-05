import sys; sys.path.append('.') # Rajouter le repertoire courant
from b300116670 import selectionSort
test = selectionSort( [5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10] 
if  test:
     print('--------------------')
     print(':tada: :tada: :tada:')
else:
     print('--------------------')
     print(':no_entry: :no_entry: :interrobang:')
