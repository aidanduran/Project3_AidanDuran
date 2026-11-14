import random

words = ["diary", "sauce", "trees", "chair", "sandy"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6