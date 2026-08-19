# Your task is to create a program which will play Rock Paper Scissors with the user.
# Take input from the user for his/her selection like scissors/rock/paper. 
# Program should select randomly rock/paper/scissors. Output should be indicating who won the user or computer. 

import random

def rock_paper_scissors():
    choices = ["r","p","s"]
    while True:
        play = str(input("Want to play again\nY for Yes and N for No:").lower().strip())
        if play == "y":
            computer = random.choice(choices)
            print("R for Rock   P for Paper    S for Siccors")
            try:   
                user = str(input("Enter your selection:").lower().strip())
                if user == computer:
                    print("Tied.")
            
                elif user == "p" and computer == "r" \
                or user == "r" and computer == "s" \
                or user == "s" and computer == "p":
                    print("User won!.")
           
                elif computer == "s" and user == "p" \
                    or computer == "p" and user == "r" \
                    or computer == "r" and user == "s":
                    print("computer won!.")
                else:
                    print("Invalid input.")
            except Exception as e:
                print(f"Error occured: {e}")
        elif play == "n":
            print("Game end!.")
            break
        else:
            print("Invalid input.")
            break

rock_paper_scissors()
