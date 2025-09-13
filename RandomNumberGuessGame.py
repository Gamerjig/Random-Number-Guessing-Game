import random as rand
import os

def clear():
    os.system("cls")

while True:
    clear()
    print("Welcome to my Random number guessing game!")
    print("Made by Gamerjig!")
    print("Can be from 0 to 10")
    
    
    rn = str(rand.randint(0, 10))
    pa = str(input("Enter your guess: "))
    
    clear()
    
    if pa == rn:
        print("You win!")
    else:
        print("You lost..")
    
    print("You guessed "+ pa + " the number was " + rn)
    print("Play again?")
    print("1 - Yes")
    print("2 - No")
    again = str(input("Enter your choose: "))
    if again == "1":
        print("Restarting")
    elif again == "2":
        break
    else:
        print("1 for yes")
        print("2 for no")
