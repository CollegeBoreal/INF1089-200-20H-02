#!/bin/sh

# --------------------------------------
# Spec (test) specific file
# Use this to customize the testing files
# code: Binary Search 
# --------------------------------------

generate_spec () {
   echo "import sys; sys.path.append('.') # Rajouter le repertoire courant" > .scripts/b${id}.spec.py
  
   echo "from b${id} import primes" >> .scripts/b${id}.spec.py
   echo "test = list(takewhile(lambda x: x < 60, primes())) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59] " >> .scripts/b${id}.spec.py
   echo "if  test:" >> .scripts/b${id}.spec.py
   echo "     print('--------------------')" >> .scripts/b${id}.spec.py
   echo "     print(':tada: :tada: :tada:')" >> .scripts/b${id}.spec.py
   echo "else:" >> .scripts/b${id}.spec.py
   echo "     print('--------------------')" >> .scripts/b${id}.spec.py
   echo "     print(':no_entry: :no_entry: :interrobang:')" >> .scripts/b${id}.spec.py
}

