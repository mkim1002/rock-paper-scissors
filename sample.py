#Rock,Paper,scisor 
from random import randint
#player_option
po = ['Rock','Paper','Scissors']
com = po[randint(0,2)]

p = False
while p == False:
    p = input('Rock, Paper, Scissors?')
    if p==com:
        print("Tie!")
    elif p == "Rock":
        if com == "Paper":
            print("You lose!", com, "covers", p)
        else:
            print("You win!", p, "smashes", com)
    elif p == "Paper":
        if com == "Scissors":
            print("You lose!", com, "cut", p)
        else:
            print("You win!", p, " covers", com)
    elif p == "Scissors":
        if com == "Rock":
            print("You lose!", com, "smashes", p)
        else:
            print("You win!", com, "cut", p)
    else:
        print("That's not a valid play. Check your spelling!")
    p = False
    com = po[randint(0,2)]





