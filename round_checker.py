import random

# Function go here


def check_rounds():

    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # If response is not an integer go back to
            # start to loop
            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):

        valid = False
        while not valid:

            # Ask user for choice (and out choice in lowercase)
            response = input(question).lower()

            # iterates through list and if response is an item
            # in the list (or the first letter of an item), the
            # full item name is returned

            for item in valid_list:
                if response == item[0] or response == item:
                    return item

            # output error if item not in list
            print(error)
            print()

# Main routine goes here

# Lists of valid response
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("The rule of this game is to pick the number of rounds that you want to play against the computer "
          ", when the game starts pick from rock, paper and scissors or (r / p / s)"
          ", or you can play the continues mode where you can play an unlimited amount and to stop you press xxx"
          ", I hope you enjoy this game and good luck")
    print()

# If 'yes', show instructions


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


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


def start():
    print()
    print("lets get started")
    print()
    prize_decoration = "-"
    return""

statement_generator("Welcome to Rock, Paper and scissors", "*")
print()

played_before = yes_no("Have you played the ""game before? ")

if played_before == "no":
    instructions()

if played_before == "yes":
    start()

# ask user for # of rounds then loop...

game_summary = []

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Ask user # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
    print()

    if rounds == "":
        heading = "Rounds {} of: " \
                    "{}".format(rounds_played + 1, rounds)

        # end rounds if necessary
        if rounds_played == rounds:
            break

    # Prints round info...
        print(heading)
