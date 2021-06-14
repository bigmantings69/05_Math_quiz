import random


# instruction if user did not play the game before


def instructions():
    print()
    print("**** How to Play ****")


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


def check_rounds():

    while True:
        response = input("How many rounds: ")

        round_error = "Please type in an integer"

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

# maths quiz list for the program
yes_no_list = ["yes", "no"]
mq_list = ["add", "subtract", "multiply", "+", "-", "*", "xxx"]
difficulty_list = ["easy", "hard"]


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
statement_generator("Welcome to Math quiz", "*")
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

if played_before == "yes":
    start()

# ask user for # of rounds then loop...

game_history = []

how_many = 1
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0


# Ask user # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        round_heading = "Continues Mode: " \
                "Round {}".format(rounds_played)

    else:
        heading = "Round {} ".format(rounds_played + 1)
    statement_generator(heading, "-")

    if rounds_played == rounds:
        break

    rounds_played += 1

    # for item in range(0, 5):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    num_3 = random.randint(10, 20)
    num_4 = random.randint(1, 10)
    symbol = ("+", "-", "*")
    operation = random.choice(symbol)

    # Prints round info...
    print(heading)

    # Get user choice...
    choose_instruction = "Please choose add (+), subtract (-)" \
                         "or multiply (*), press (enter) for random or 'xxx' to quit"
    print()
    choose_error = "Please choose from add (+) subtract (-) " \
                   "or multiply (*), press (enter) for random (or xxx to quit)"

    diff_instructions = "What difficulty would you like to play with?? "
    diff_error = "Please choose 'easy' or 'hard' "

    diff_choice = choice_checker(diff_instructions, difficulty_list, diff_error)
    print("you chose: {}".format(diff_choice))

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, mq_list,
                                 choose_error)

    # End game if exit code is typed

    if user_choice == "xxx":
        print("So you have changed your mind, come on play the game", "LLL")
        break

    question = "{} {} {}".format(num_1, operation, num_2)
    answer = eval(question)

    print("question: ", question)

    if user_choice == answer:
        result = "won"

    else:
        result = "lost"
        rounds_lost += 1

        for item in range(1, how_many + 1):

            if user_choice == "xxx":
                round_result = ""
            if user_choice == "xxx":
                percent_win = "0%"
                rounds_won = "0"
            if result == "won":
                feedback = "you won"

            else:
                feedback = "you lost"
            round_result = "Round {}: {}".format(rounds_played, feedback)
            game_history.append(round_result)

    # Ask user if they want to see their game history.
    # If 'yes' show game game history

    # Show game statistics
rounds_won = rounds_played - rounds_lost

rounds_lost = rounds_played - rounds_won

# **** Calculate Game Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("***** Game History *****")
for item in game_history:
    print(item)

print()

    # display game stats with % values to the nearest whole number
print("******* Game statistics *******")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\n".format(rounds_won,
                                                                 percent_win,
                                                                 rounds_lost,
                                                                 percent_lose))
print()
print("Thanks for playing")







