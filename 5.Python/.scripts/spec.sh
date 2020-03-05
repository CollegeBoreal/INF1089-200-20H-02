#!/bin/sh

# --------------------------------------
# Spec (test) specific file
# Use this to customize the testing files
# code: Binary Search 
# --------------------------------------

generate_spec () {
   echo "import sys; sys.path.append('.') # Rajouter le repertoire courant" > .scripts/b${id}.spec.py
  
   echo "from b${id} import selectionSort" >> .scripts/b${id}.spec.py
   echo "test = selectionSort( [5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10] " >> .scripts/b${id}.spec.py
   echo "if  test:" >> .scripts/b${id}.spec.py
   echo "     print('--------------------')" >> .scripts/b${id}.spec.py
   echo "     print(':tada: :tada: :tada:')" >> .scripts/b${id}.spec.py
   echo "else:" >> .scripts/b${id}.spec.py
   echo "     print('--------------------')" >> .scripts/b${id}.spec.py
   echo "     print(':no_entry: :no_entry: :interrobang:')" >> .scripts/b${id}.spec.py
}

