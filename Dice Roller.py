import random

while True:
    pass

    print ("Rolling Dice...")
    print(f"The value is", random.randint(1, 6))

    repeat = input("Roll dice again? 'y' for yes and 'n' for no: ")
    if repeat == 'n':
        break