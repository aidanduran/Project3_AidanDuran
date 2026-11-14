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
        print(display)
        return "win"
    if incorrect_guesses == max_guesses:
        print("Sorry! You ran out of guesses.")
        print("The secret word was:", secret_word)
        return "lose"
    return "continue"

def play_game():
    global incorrect_guesses
    while True:
        display_word()
        print(f"Guessed letters: {guessed_letters}")
        print(f"Incorrect guesses remaining: {max_guesses - incorrect_guesses}")
        guess = input("Please enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

        status = check_game_status()
        if status != "continue":
            break

play_game()