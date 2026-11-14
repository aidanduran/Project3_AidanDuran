import random

words = ["diary", "sauce", "trees", "chair", "sandy"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

def display_word():
    print("Secret word:")
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += f"{letter} "
        else:
            display += "_ "
    print(display)