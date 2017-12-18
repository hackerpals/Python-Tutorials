#!/usr/bin/env python3


import random

PROMPT = "What is your guess? "

#New Constants
QUIT = -1
QUIT_TEXT = 'q'
QUIT_MESSAGE = 'Thank you for playing'
CONFIRM_QUIT_MESSAGE = 'Are you sure you want to quit (Y/n)? '


# New confirm_quit function
def confirm_quit():
    """Ask use to confirm that they want to quit
    default to yes
    Return True (yes, quit) or False (no, don't quit)"""
    spam = input(CONFIRM_QUIT_MASSAGE)
    if spam == 'n':
        return False
    else:
        return True

def do_guess_round():
    """Choose a random number, ask the user for a guess
    check wheather the guess is true
    and repeat until the user is correct """
    computer_number = random.randint(1,100)
    number_of_guessess = 0

    while True:
        players_guess = input(PROMPT)
        # new if clause to test against quit
        if players_guess == QUIT_TEXT:
            if confirm_quit():
                return QUIT
            else:
                continue

        number_of_guessess = number_of_guessess + 1
        if computer_number == int(players_guess):
            print('Correct!')
            return number_of_guessess
        elif computer_number > int(players_guess):
            print('Too Low')
        else:
            print("Too High")

total_rounds = 0
total_guesses = 0

while  True:
    total_rounds = total_rounds +1
    print("Starting round number: " + str(total_rounds))
    print("Let the guessing begin!!!")
    this_round = do_guess_round()

    if this_round == QUIT:
        total_rounds = total_rounds - 1
        avg = str(total_guesses/float(total_rounds))
        if total_rounds == 0:
            stats_message = 'You completed no rounds. \n  Please try again later'
        else:
            stats_message = 'You played ' + str(total_rounds) + '\n' + ' rounds, with average of ' + str(avg)
        break

    total_guesses = total_guesses+this_round
    avg = str(total_guesses/float(float_rounds))
    print("You took "+str(this_round)+" guesses")
    print("Your guessing average = "+str(avg))
    print("")


print(stats_message)
