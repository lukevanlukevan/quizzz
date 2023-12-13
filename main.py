import os
import random
from questions import questions
import logging as l

qq = questions

total = len(qq)
indexes = ["A", "B", "C", "D"]
score = 0
q_num = 0


def check_answer(answers, correct, response):
    global score
    global q_num

    os.system('clear')

    pickedindex = indexes.index(response)
    correctindex = answers.index(correct)

    if pickedindex == correctindex:
        os.system('clear')
        print("Correct!")
        score += 1
    else:
        print("Answer was incorrect")

    input("Press enter to continue")

    q_num += 1

    qq.pop(0)


def give_question(ques):
    global score
    os.system('clear')
    print(len(qq))

    print(f'Score: {score}\n')

    print(f'Question {q_num + 1}')

    question = ques["question"]

    answers = ques["answer"]
    random.shuffle(answers)

    correct = ques["correct_answer"]

    print(question)

    astring = ""
    for i, a in enumerate(answers):
        iterator = indexes[i]
        astring += f"{iterator}. {a}\n"

    print(astring)

    response = input("Please enter the correct letter: ").upper()

    if response in indexes:
        check_answer(answers, correct, response)
    else:
        os.system('clear')
        print("Please enter a valid answer (A, B, C or D)")
        input("Press enter to continue")


def end_card():
    os.system('clear')
    print("🏆🏆🏆")
    print(f"You have finished the quiz!\nYour final score was {score}/{total}")


def run_quiz():
    global qq
    while len(qq) > 0:
        q = qq[0]
        give_question(q)

    if len(qq) == 0:
        end_card()
        print('\n')
        input("Press enter to return to main menu.")
        main_menu()

# ------------------


def show_rules():
    os.system('clear')
    print("Rules:\n")
    print("You will be asked a series of questions about Harry Potter.")
    print("You will be presented with 4 possible answers.")
    print("You must enter the letter of the correct answer.")
    print("You will be told if you are correct or not.")
    print("\n")
    option = input("Press enter to return to main menu.")
    main_menu()


def main_menu():
    global qq
    os.system('clear')
    menu = ['Start', 'Rules', 'Exit']
    score = 0
    menustring = ""
    for i, a in enumerate(menu):
        iterator = indexes[i]
        menustring += f"{iterator}. {a}\n"

    print(menustring)

    menuselect = input(f"Please select an option: ").upper()

    if menuselect == "A":
        qq = basequestions
        run_quiz()
    elif menuselect == "B":
        show_rules()
    elif menuselect == "C":
        print("Goodbye!")
        exit()


main_menu()
