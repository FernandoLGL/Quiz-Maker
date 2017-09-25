from random import shuffle
import os
import sys


class Question(object):

    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options


def get_sets(file):
    file.seek(0)
    out = []
    t = file.read().split("\n")[:-1]
    for elem in t:
        out.append(elem.split('--'))
    return out


def clear_screen():
    '''
    Clear screen
    '''
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system('clear')
    elif sys.platform == "win32":
        os.system('cls')


def menu():
    # Handling the file at the beginning
    try:
        a = open('scores.txt', 'r')
        reading = a.read()
        a.seek(0)
        f = open('scores.txt', 'w+')
        f.write(reading)
    except:
        print("The file doesn't exist. Creating it now. Please write the questions on it following the instructions,  then try again.")
        f = open('scores.txt', 'w+')
        return

    sets = get_sets(f)
    correct = 0
    number_of_questions = len(sets)

    while sets != []:
        clear_screen()
        q = Question(sets[-1][0], sets[-1][1], sets[-1][2:])
        sets.pop()
        print (q.question)
        for count, option in enumerate(q.options):
            print(str(count + 1) + ". " + option)
        answer = input("What's your answer? Pick a number.\n")
        if answer == q.answer:
            correct += 1

    total = (correct / number_of_questions) * 10

    print("\nYour grade: ", total, "\nNumber of correct answers:", correct, 'out of', number_of_questions)


menu()
