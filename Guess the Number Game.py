import random

max_num = 30

random_number = random.randint(1, max_num)

guess = 0

while guess != random_number:
    guess = int(input(f"Enter a number between 1 and {max_num}: "))
    if guess < random_number:
        print("Wrong! Too low...")
    elif guess > random_number:
        print("Wrong! Too high...")

print(f"You guessed it! The number indeed was {random_number}.")