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


# statement generator to decorate the program
def statement_generator(outcome, prize_decoration):

    sides = prize_decoration * 3

    outcome = "{} {} {}".format(sides, outcome, sides)
    top_bottom = prize_decoration * len(outcome)

    print(top_bottom)
    print(outcome)
    print(top_bottom)

    return ""


def start():

    print()
    print("lets get started")
    print()
    prize_decoration = "-"
    return""

# ask user if they have played before and display instructions if necessary
statement_generator("Welcome to Higher or lower", "*")
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

if played_before == "yes":
    start()
