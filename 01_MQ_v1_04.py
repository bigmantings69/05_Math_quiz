import random


# instruction if user did not play the quiz before


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


def int_check(question, low=None, high=None, exit_code=None):

    while True:

        response = input(question).lower()
        exit_code = "xxx"
        if exit_code == "xxx" and response == "xxx":
            return response
        elif exit_code == "xxx" and response == "":
            return response

        situation = ""

        if low is not None and high is not None:
            situation = "both"
        elif low is not None and high is None:
            situation = "low only"
        try:
            response = int(response)

            # check input is not too high or
            # too low if a both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("please enter a number between "
                          "{} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more "
                          "than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is a integer

        except ValueError:
            print("Please enter an integer")
            continue


def choice_checker(question):

    error = "Please choose from (+), (-), (*)" \
            " or xxx to quit"

    valid = False
    while not valid:

        # Ask user for choice (and out choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned
        if response == "+":
            return "+"
        elif response == "-":
            return "-"
        elif response == "*":
            return "*"
        elif response == "xxx":
            return response
        else:
            print(error)


def diff_checker(question, valid_list):

    diff_error = "Please choose from easy or hard"

    valid = False
    while not valid:

        # Ask user for choice (and out choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned
        if response == "e" or response == "easy":
            return "easy"
        elif response == "h" or response == "hard":
            return "hard"
        else:
            print(diff_error)

        for item in valid_list:
            if response == item[0] or response == item:
                return item

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

played_before = yes_no("Have you done this quiz before? ")

if played_before == "no":
    instructions()

if played_before == "yes":
    start()


# ask user for # of questions then loop...

quiz_summary = []

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# maths quiz list for the program

yes_no_list = ["yes", "no"]
mq_list = ["+", "-", "*"]
difficulty_list = ["easy", "hard"]

# Ask user # of rounds, <enter> for infinite mode

rounds = int_check("Enter number of questions: ", 1, exit_code="")

diff_instructions = "What difficulty would you like to play with?? "
diff_error = "Please choose 'easy' or 'hard' "

diff_choice = diff_checker(diff_instructions, difficulty_list)
print("you chose: {}".format(diff_choice))

# Ask user for choice and check it's valid

operation = choice_checker("Please pick from +, -, * or xxx to quit")

end_quiz = "no"
while end_quiz == "no":

    # Start of quiz Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        round_heading = "Continues Mode: " \
                "question {}".format(rounds_played)

    else:
        heading = "Question {} ".format(rounds_played + 1)
        statement_generator(heading, "-")
        print()

    if rounds_played == rounds:
        break

    rounds_played += 1

    # for item in range(0, 5):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(10, 20)
    num_3 = random.randint(5, 10)
    num_4 = random.randint(1, 5)

    # Prints round info...

    # End quiz if exit code is type

    if diff_choice == "easy":
        question = "{} {} {}".format(num_3, operation, num_4)
        answer = eval(question)

    else:
        question = "{} {} {}".format(num_1, operation, num_2)
        answer = eval(question)

    print("question: ", question)

    result = int_check("Answer: ", exit_code="")
    if result == "xxx":
        print("So you have changed your mind, come on do the quiz", "LLL")
        break
    if result == answer:
        print("Correct")
        feedback = "Correct"
    else:
        print("Incorrect")
        feedback = "Incorrect"

    # Output results...
    round_result = "question {}: {}".format(rounds_played, feedback)

    quiz_summary.append(round_result)

    # end quiz if requested # of question has been played
    if rounds_played == rounds:
        break

    # Show quiz statistics
rounds_won = rounds_played - rounds_lost - rounds_drawn

# **** Calculate quiz Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("***** Quiz History *****")
for game in quiz_summary:
    print(game)

print()
print("Thanks for playing")