import random

set_words = ["Python", "Pandas", "Numpy", "SQL", "Repository", "Git", "Github"]


random_word = random.choice(set_words)
print(random_word)

guess_word = ['_']* len(random_word)
num_try = 6
user_guess = [] # store the user input

print("Welcome to Hangman Game!")

while num_try > 0  and '_' in guess_word:
    print("\nWord:", ''.join(guess_word))
    print(f"You have {num_try} attempts left")
    print("User's guess:", ','.join(user_guess))
    guess_try = input("Please guess a letter: ").lower()
    if guess_try not in user_guess:
        user_guess.append(guess_try)

    if guess_try in random_word.lower():
        for i in range(len(random_word)):
            if random_word[i].lower() == guess_try:
                guess_word[i] = random_word[i]
        print("You guessed it right!")
    else:
        num_try -= 1
        print(f"Wrong guess!")

if '_' not in guess_word:
    print(f"You guessed the word! {random_word}")
else:
    print(f"Game over! The word is : {random_word}")