from random import shuffle
import os
import sys


class Question(object):
    # Simple 'Question' class
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options


def get_sets(file):
    '''
    Function which does the same as Python's .readlines().split('--').
    '''
    file.seek(0)  # returning the cursor to the beginning
    out = []  # defining the output
    t = file.read().split("\n")[:-1]  # Doing the .readlines() magic. Splitting by CR+LF and excluding the last item.
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
        a = open('questions.txt', 'r')
        reading = a.read()
        a.seek(0)
        f = open('questions.txt', 'w+')
        f.write(reading)
    except:
        print("The file doesn't exist. Creating it now. Please write the questions on it following the instructions,  then try again.")
        f = open('questions.txt', 'w+')
        return

    # The needed grade is the first line of the file
    needed_score = float(get_sets(f)[0][0])
    # The sets, which are lists, will be everything after the first line
    sets = get_sets(f)[1:]
    # number of correct answers
    correct = 0
    # self-explanatory
    number_of_questions = len(sets)

    while sets != []:
        clear_screen()
        shuffle(sets) #randomize
        q = Question(sets[-1][0], sets[-1][1], sets[-1][2:])  # Always using the last 'set' as a reference
        sets.pop()  # We are treating 'sets' as a stack. Popping and not caring about the return.
        print (q.question)
        for count, option in enumerate(q.options):  # tuple unpacking to easily get the numbers
            print(str(count + 1) + ". " + option)
        answer = input("What's your answer? Pick a number.\n")
        if answer == q.answer:
            # If the answer is correct, add 1 to 'correct', otherwise just proceed with the while loop.
            correct += 1
    # calculating the score
    score = (correct / number_of_questions) * 10

    # printing the results
    print("\nYour grade:", score, "\nNumber of correct answers:", correct, 'out of', number_of_questions)
    print("You needed", str(needed_score), "and you got", score)
    if score >= needed_score:
        print("\n\tCongrats! You passed.")
    else:
        print("\n\tOops, looks like you didn't get enough of them right. Sorry!")


menu()
