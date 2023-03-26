# Rock Scissor Paper Game
import random
import os
import time

def gameWin():
    if user==comp:
        return None
    else:
        if user=="r" and comp =="s" or user=="s" and comp =="p" or user=="p" and comp =="r":
            return True
        else:
            return False

def compChoice():
    print("Computer's turn:")
    time.sleep(y)
    print (".")
    time.sleep(x)
    print (".")
    time.sleep(x)
    print (".")
    time.sleep(x)
    print ("Computer made it's choice.\n")

lookup={
    0: "r",
    1: "s",
    2: "p",
    "r": "Rock",
    "s": "Scissor",
    "p": "Paper"
}
replay = ""
while replay!="q":
    os.system('cls')
    x=0.1
    y=1
    
    print ("\t\t***ROCK SCISSOR PAPER***\n\n")
    time.sleep(x)
    
    compChoice()
    
    user=" "
    while user!="r" and user!="s" and user!="p":
        user = (input("Your turn:\nRock(r), Scissor(s), Paper(p)? ")).lower()
    time.sleep(x)
    
    rand=random.randint(0,2)
    comp = lookup[rand]
    time.sleep(y)
    print(f"\nYou chose      : {lookup[user]}")
    time.sleep(y)
    print(f"\nComputer chose : {lookup[comp]}\n")
    time.sleep(y)
    
    if gameWin()==None:
        print("TIE !!")
    elif gameWin():
        print("YOU WIN !!")
    else:
        print("YOU LOSE !!")
    time.sleep(y)
    
    replay = input("\n\nPlay again?\n\nPress any key to continue,\nPress 'q' to quit.\n")