from turtle import *
from time import sleep

play = "y"
while play == "y":
    sides = int(input("How many sides will the shape have?"))

    for side in range(sides):
        forward(50)
        left((360/sides))
        sleep(0.2)
    play = str(input("Would you like to play again? Press y or n: "))
