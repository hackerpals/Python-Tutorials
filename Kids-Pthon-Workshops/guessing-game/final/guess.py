import random #Imports the random module

RandNum = random.randint(1,100)
guess = 'Guess A Number between 1 and 100: ' # Craete a string

while True:
    player_guess = input(guess)

    if RandNum == int(player_guess):
        print('Correct Woohoo!')
        break #If the answer is correct it will break the statement

    elif RandNum > int(player_guess):
        print("Sorry! Too Low")

    else:
        print("Sorry! Too High")
