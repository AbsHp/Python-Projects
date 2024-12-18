import random

def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' or computer == 'p') or (user == 'p' and computer == 'r'):
        return True

def rock_paper_scissors():
    player = input("What is your choice - 'r' for rock, 's' for scissors and 'p' for paper: ")
    choices = ['r', 's', 'p']
    opponent = random.choice(choices)

    if player == opponent:
        return print(f"Its a tie. My Choice was {opponent}.")
    
    if check_win(player, opponent):
        return print(f"Yay, you won! My choice was {opponent}.")
    
    if check_win(player, opponent) != True:
        return print(f"You lost. My choice was {opponent}.")

rock_paper_scissors()