import random
from time import sleep

FLASHCARD_FILENAME = "flashcards.txt"
questions = {}


def clear_terminal():
    print(chr(27) + "[2J")


def add_question(question, answer):
    try:
        questions[question][0] += 3
    except KeyError:
        questions[question] = [3, answer.strip().lower()]


def load_file():
    with open(FLASHCARD_FILENAME) as f:
        for line in f:
            add_question(*line.split(' : '))


def save_file():
    with open(FLASHCARD_FILENAME, 'w') as f:
        for question, info in questions.items():
            output = question + ' : ' + info[1] + '\n'
            for _ in range((info[0] + 2) // 3):
                f.write(output)


def add_flashcard():
    add_question(
        input("Enter the question for the new flashcard: "),
        input("Enter the answer for the new flashcard: ")
    )


def view_flashcard():
    clear_terminal()

    try:
        question = random.choice(list(questions.keys()))
    except IndexError:
        print("We have run out of questions.")
        raise KeyboardInterrupt

    answer = questions[question][1]
    correct = input(question + " ").lower() == answer
    print("{0}[32mCorrect!{0}[0m".format(chr(27))
          if correct else
          "The correct answer was: '{}'".format(answer))

    info = questions[question]
    if not correct:
        info[0] += 3
    else:
        info[0] -= 1
        if not info[0]:
            del questions[question]

    sleep(2 if not correct else 0.5)


def main():
    while True:
        tmp = int(input("\nEnter 0 to add flashcards, 1 to view them: "))
        action = [add_flashcard, view_flashcard][tmp]
        try:
            while True:
                action()
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    load_file()
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + chr(27) + "[36m goodbye!" + chr(27) + "[0m")
    finally:
        save_file()