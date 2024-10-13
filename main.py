import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # You have 10 attempts to guess the number

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("Your guess is out of bounds. Try a number between 1 and 100.")
        elif guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")

if _name_ == "_main_":
    guess_the_number()