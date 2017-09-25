from random import shuffle


def get_sets(file):  # generator that yields each set of question/answer/options
    file.seek(0)
    t = file.read().split("\n")[:-1]
    for elem in t:
        yield elem.split('--')


def get_questions(file):  # generator that yields the questions
    for elem in get_sets(file):
        yield elem[0]


def get_answers(file):
    for elem in get_sets(file):
        yield elem[1]


def get_options(file):
    # yields 'n' lists which are the options for 'n' questions.
    for elem in get_sets(file):
        yield elem[2:]


def menu():
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

    while True:
        number_of_questions = len(list(get_questions(f)))
        correct = 0
        while True:
            for question in get_questions(f):
                print(question)


menu()
