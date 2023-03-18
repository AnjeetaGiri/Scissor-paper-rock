import random
def play():
    user=input("What's your choice?'r' for rock,'s' for scissors,'p' for paper\n")
    computer=random.choice(['r','s','p'])
    if user==computer:
        return "Tie!"
    if is_win(user,computer):
        return "You won!!!"
    return "You lost!"        

def is_win(player,opponent):
    if(player=='r'and opponent=='p') or (player=='s' and opponent=='r')or (player=='p' and opponent=='s'):
        return True
print(play())      
