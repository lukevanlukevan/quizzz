import os
import random
from questions import questions

qq = questions
total = len(qq)
indexes = ["A", "B", "C", "D"]
score = 0


def check_answer():
    input("Continue? (Press enter)")
    pass


def give_question(ques):
    global score
    os.system('clear')

    print(f'Score: {score}\n')

    question = ques["question"]
    answers = ques["answers"]
    random.shuffle(answers)
    correct = ques["correct"]

    print(question)
    astring = ""
    for i, a in enumerate(answers):
        iterator = indexes[i]
        astring += f"{iterator}. {a}\n"

    print(astring)
    response = input("Please enter the correct letter: ").upper()

    if response in indexes:
        pickedindex = indexes.index(response)
        correctindex = answers.index(correct)
    else:
        pickedindex = None
        correctindex = None

    if not response in indexes:
        os.system('clear')
        print("Please enter a valid letter")
    if pickedindex == correctindex:
        os.system('clear')
        print("Correct!")
        score += 1
    else:
        print("unknown error")

    qq.pop(0)


def end_card():
    os.system('clear')
    print("🏆🏆🏆")
    print(f"You have finished the quiz!\nYour final score was {score}/{total}")


def run_quiz():
    while len(qq) > 0:
        q = qq[0]
        give_question(q)

    if len(qq) == 0:
        end_card()
        print('\n')
        main_menu()

# ------------------


def main_menu():
    os.system('clear')
    menu = ['Start', 'Exit']
    score = 0
    menustring = ""
    for i, a in enumerate(menu):
        iterator = indexes[i]
        menustring += f"{iterator}. {a}\n"

    print(menustring)

    menuselect = input(f"Please select an option:").upper()

    if menuselect == "A":
        run_quiz()
    elif menuselect == "B":
        print("Goodbye!")
        exit()


main_menu()
