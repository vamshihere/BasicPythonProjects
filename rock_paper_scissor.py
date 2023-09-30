import random

def play():
    user = input(" enter 'r' for rock, 'p' for paper and 's' for scissor : ")
    comp = random.choice(['r','p','s'])
    if(win(user,comp) == 1):
        return "you won"
    elif(win(user,comp) == 0):
        return "it's a tie"
    else:
        return "you lost"

def win(user,comp):
    if(user == comp):
        return 0
    elif((user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p')):
        return 1
    else:
        return -1

print(play())    