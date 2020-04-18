import random

fortunes = ['Definitely!', 'Very Likely', 'Maybe', 'It seems so', 'Doubtful', 'No way!', "Don't count on it",
            'Answer hazy, try again']

repeat = True
while repeat == True:
    print('The Magic 8 Ball is said to have the mystical power of fortune telling. It can peer through the mists and divine'
      ' the answer to any yes or no question. What would you ask of the Magic 8 Ball?')
    input()
    print("The mist clears, revealing the Magic 8 Ball's answer:")
    print(fortunes[random.randint(0, 8)])
    print("Would you like to ask another question? Type Y for yes or press enter to end your session.")
    another_question = input()
    if another_question in ['Y', 'y', 'Yes', 'yes']:
        continue
    else: break
