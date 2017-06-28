# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

choices = ['Rock', 'Paper', 'Scissors']
while True:
    inp = input("Rock Paper Scissors, type q to quit: ")
    computer_choice = random.choice(choices)


    def determine_winner(inp, computer_choice):
        condition1 = (inp == 'Rock' or computer_choice == 'Rock') and \
                     (inp == 'Scissors' or computer_choice == 'Scissors')

        condition2 = (inp == 'Rock' or computer_choice == 'Rock') and \
                     (inp == 'Paper' or computer_choice == 'Paper')

        condition3 = (inp == 'Scissors' or computer_choice == 'Scissors') and \
                     (inp == 'Paper' or computer_choice == 'Paper')

        if condition1:
            if inp == 'Rock': winner = 'Player'
            else: winner = 'Computer'
            return winner

        elif condition2:
            if inp == 'Paper': winner = 'Player'
            else: winner = 'Computer'
            return winner

        elif condition3:
            if inp == 'Scissors': winner = 'Player'
            else: winner = 'Computer'
            return winner

        else:
            print('Please enter a proper input')
            return

    if inp == computer_choice:
        print('Tie!')

    elif inp == 'q': break

    else:
        print('The winner is ' + determine_winner(inp, computer_choice) + "\n" +
              'Player = {} || Computer = {}'.format(inp, computer_choice) + "\n")
