import random 

name = input("Quel est ton nom? ") 

print("Bonne Chance ! ", name) 

words = ['rainbow', 'ordinateur', 'science', 'programmation', 
		'python', 'mathematiques', 'joueur', 'condition', 
		'reverse', 'eau', 'planche', 'geeks'] 

word = random.choice(words) 


print("Devinez les lettres") 

guesses = '' 

turns = 12


while turns > 0: 
	
	failed = 0
	
	for char in word: 
		
		if char in guesses: 
			print(char) 
			
		else: 
			print("_") 
			
			failed += 1
			

	if failed == 0: 
		print("Tu gagnes") 
		
		print("Le mot est: ", word) 
		break
	
	guess = input("Devinez un lettre:") 
	
	guesses += guess 
	
	if guess not in word: 
		
		turns -= 1
		
		print("Faux") 
		

		print("Tu as", + turns, 'more guesses') 
		
		
		if turns == 0: 
			print("Perdant") 