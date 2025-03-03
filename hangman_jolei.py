import random

set_words = ["Python", "Pandas", "Numpy", "SQL", "Repository", "Git", "Github"]


random_word = random.choices(set_words)
print(random_word)

guess_word = ['_']* len(random_word)
num_try = 6

print("Welcome to Hangman Game!")

