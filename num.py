import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 20.")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess_text = input("Enter your guess: ")

    if not guess_text.isdigit():
        print("Please enter a valid whole number.")
        continue

    guess = int(guess_text)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Well done! You guessed the number in {attempts} tries.")
        break
