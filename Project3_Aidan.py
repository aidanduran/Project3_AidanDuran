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

def check_game_status():
    for letter in secret_word:
        if letter not in guessed_letters:
            break
    else:
        print("Congratulations! You guessed the word!")
        print("Final word:")
        display = ""
        for letter in secret_word:
            display += f"{letter} "

        print()
        return "win"

    if incorrect_guesses == max_guesses:
        print("Sorry! You ran out of guesses.")
        print("The secret word was:", secret_word)
        return "lose"

    return "continue"