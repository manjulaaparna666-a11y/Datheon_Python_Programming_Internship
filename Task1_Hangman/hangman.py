import random

words = ["python", "internship", "datheon", "hangman", "developer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord: ", " ".join(guessed))
    print(f"Attempts left: {attempts}")
    print(f"Used letters: {used_letters}")
    
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("Already guessed!")
        continue
    
    used_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        print("Wrong!")
        attempts -= 1

if "_" not in guessed:
    print(f"\nYou Won! The word was: {word}")
else:
    print(f"\nYou Lost! The word was: {word}")
