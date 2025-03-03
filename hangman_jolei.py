import random

set_words = ["Python", "Pandas", "Numpy", "SQL", "Repository", "Git", "Github"]


random_word = random.choices(set_words)
print(random_word)

def chosen_word(set_words, guess_let):
    show_let = ""
    for letter in random_word:
        if letter in guess_let:
            show_let += letter
        else:
            show_let += "_"
    return show_let

def hangman_game():
    max_try = 7
    guess_let= []
    guess_word = random_word
    attempts = 0

