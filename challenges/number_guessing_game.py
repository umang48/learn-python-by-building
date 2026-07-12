import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        break