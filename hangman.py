import random

words = ["python", "internship", "datheon", "hangman", "developer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used = []

print("Welcome to Hangman Game! ID: DT-2026-NVYUF")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print(f"Attempts left: {attempts}")
    ch = input("Guess a letter: ").lower()
    
    if ch in word:
        for i, l in enumerate(word):
            if l == ch:
                guessed[i] = ch
    else:
        attempts -= 1

if "_" not in guessed:
    print(f"You Won! Word was: {word}")
else:
    print(f"Game Over! Word was: {word}")
