import math
import random


# instruction if user did not play the game before


def instructions():
    print()
    print("**** How to Play ****")
    print("Good Luck!")

# yes or no answer for the program
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please enter yes or no")

# ask user if they have played before and display instructions if necessary
statement_generator("Welcome to Higher or lower", "*")
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

if played_before == "yes":
    start()

