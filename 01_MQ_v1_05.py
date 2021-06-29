import random


# instruction if user did not play the quiz before


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("This is a quiz where you will need to enter 'easy' or 'hard' mode")
    print("and you will need to choose the arithmetic you will need to get as")
    print(" many correct answers as you can")
    print()
    print("Good Luck")
    print()

# integer checker which has the xxx and it checks for integers


def int_check(question, low=None, high=None, exit_code=None):

    while True:

        response = input(question).lower()

        if exit_code == "xxx" and response == "xxx":
            return response
        elif exit_code == "" and response == "":
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

# statement generator to decorate the program


def statement_generator(outcome, prize_decoration):

    sides = prize_decoration * 3

    outcome = "{} {} {}".format(sides, outcome, sides)
    top_bottom = prize_decoration * len(outcome)

    print(top_bottom)
    print(outcome)
    print(top_bottom)

    return ""

# if user choose yes then print lets get started


def start():
    print()
    print("lets get started")
    print()
    prize_decoration = "-"
    return""

# welcome the user to this quiz
statement_generator("Welcome to Math quiz", "*")
print()


quiz_summary = []

questions_played = 0
questions_wrong = 0

# maths quiz list for the program

yes_no_list = ["yes", "no"]
mq_list = ["+", "-", "*"]
difficulty_list = ["easy", "hard"]

# ask user if they have done this before and display instructions if necessary


played_before = "Have you done this quiz before? "
round_error = "please choose 'yes' or 'no'"
round_choice = choice_checker(played_before, yes_no_list, round_error)

if round_choice == "no":
    instructions()

if round_choice == "yes":
    start()

# ask the user to enter number of questions


questions = int_check("Enter number of questions: ", 1, exit_code="")

# ask the user for the difficulty and run the chosen difficulty


diff_instructions = "What difficulty would you like to play with?? "
diff_error = "Please choose 'easy' or 'hard' "

diff_choice = choice_checker(diff_instructions, difficulty_list, diff_error)
print("you chose: {}".format(diff_choice))

# Ask user to pick the arithmetic and run the chosen arithmetic

operation_question = "Please pick from +, -, * or xxx to quit"
operation_error = "Please choose from (+), (-), (*)" \
            " or xxx to quit"
operation = choice_checker(operation_question, mq_list, operation_error)


end_quiz = "no"
while end_quiz == "no":

    # Start of quiz Play Loop

    # questions Heading
    print()
    if questions == "":
        heading = "Continues Mode: question {}".format(questions_played + 1)
        statement_generator(heading, "-")
        print()

    else:
        heading = "Question {} ".format(questions_played + 1)
        statement_generator(heading, "-")
        print()

    if questions_played == questions:
        break

    questions_played += 1

    # number for the quiz questions num 1 - num 2 is for hard and num 3 - num 4 is for easy
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 150)
    num_3 = random.randint(5, 10)
    num_4 = random.randint(1, 5)

    # Prints round info...

    # the quiz questions

    if diff_choice == "easy":
        question = "{} {} {}".format(num_3, operation, num_4)
        answer = eval(question)

    else:
        question = "{} {} {}".format(num_1, operation, num_2)
        answer = eval(question)

    print("question: ", question)

    # the quiz user answer

    result = int_check("Answer or 'xxx' to quit: ", exit_code="xxx")

    # End quiz if exit code is type
    if result == "xxx":
        print("So you have changed your mind, come on do the quiz")
        break
    if result == answer:
        print("Correct")
        feedback = "Correct"
    else:
        print("Incorrect")
        feedback = "Incorrect"

    # Output results...
    round_result = "question {}: {} = {} | {}".format(questions_played, question, answer, feedback)

    quiz_summary.append(round_result)

    # end quiz if requested # of question has been played
    if questions_played == questions:
        break

    # Show quiz statistics
questions_correct = questions_played - questions_wrong 

# **** Calculate quiz Stats ****

print()
print("***** Quiz History *****")
print()
for quiz in quiz_summary:
    print(quiz)

print()
print("Thanks for playing")