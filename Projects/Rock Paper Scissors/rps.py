import random

def play():
    user = input("'r' for rock, 's' for scissors, 'p' for paper ").lower()
    computer = random.choice(['r', 'p', 's'])
#the spacing in the block below matters, if the the two chunks touch then only the touching parts run
    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'A winner is you'

    return 'You lose'

def is_win(player, opponent):
    #return true if player wins
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
            return True

print(play())