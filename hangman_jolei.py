import random

set_words = ["Python", "Pandas", "Numpy", "SQL", "Repository", "Git", "Github"]


random_word = random.choice(set_words)
print(random_word)

guess_word = ['_']* len(random_word)
num_try = 6

print("Welcome to Hangman Game!")

while num_try > 0  and '_' in guess_word:
    print("\nWord:", ''.join(guess_word))
    print(f"You have {num_try} attempts left")
    guess_try = input("Please guess a letter: ").lower()

    if guess_try in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess_try:
                guess_word[i] = guess_try
        print("You guessed it right!")
    else:
        num_try -= 1
        print(f"Wrong guess!")

if '_' not in guess_word:
    print("You guessed the word!")
else:
    print(f"Game over! The word is : {random_word}")