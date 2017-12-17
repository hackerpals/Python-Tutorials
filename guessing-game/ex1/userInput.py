#!/usr/bin/env python3

'''
Title: Example 1 - User Input
This Example we explore how to request user inputs
'''


# in the python2 you can use raw_input

name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age = input("Your age? ")
print("So, you are already " + age + " years old, " + name + "!")

prompt = "What is your guess? " #This creates a variable
user_guess = input("prompt")

#You can aslo do this 
another_guess = input("Type another guess: ")
