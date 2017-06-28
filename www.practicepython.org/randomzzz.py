# Guess what number between 0 - 100 you're thinking of

import random as r

upperLimit = 100
lowerLimit = 0
guess = r.randint(0, 100)

while True:

    print(guess)
    inp = input('higher | lower | correct: \n')

    if inp == 'higher':
        lowerLimit = guess + 1

    elif inp == 'lower':
        upperLimit = guess - 1

    elif inp == 'correct':
        print('I am a very intelligent computer!\n')
        break

    try:
        guess = r.randint(lowerLimit, upperLimit)

    # ValueError is raised by the randint function if the distance between the two args is ZERO
    except ValueError:
        print('''You fucking fool, either {},{} or {} is the right number '''.format(guess-1, guess, guess+1) +
             '''or some number I've already said WHY YOU LYIN?''')