#TASK4
'''
ROCKS PAPERS SCISSORS GAME
'''

import random
l1 = ["Rocks","Paper","Scissors"]
user_score = 0
computer_score = 0

#Function to calculate the winner and the score
def winner(user,computer):
    global user_score
    global computer_score
    if user == "Rocks" and computer == "Scissors":
        print("\nThe user wins")
        user_score = user_score + 1
        print("\nYour score ",user_score)
        print("The computer score ",computer_score)
        
    elif user == "Rocks" and computer == "Paper":
        print("\nThe computer wins")
        computer_score = computer_score + 1
        print("\nYour score ",user_score)
        print("The computer score ",computer_score)

    elif user == "Scissors" and computer == "Rocks":
        print("\nThe computer wins")
        computer_score = computer_score + 1
        print("\nYour score ",user_score)
        print("The computer score ",computer_score)
    
    elif user == "Scissors" and computer == "Paper":
        print("\nThe user wins")
        user_score = user_score + 1
        print("\nYour score ",user_score)
        print("The computer score ",computer_score)

    elif user == "Paper" and computer == "Scissors":
        print("\nThe computer wins")
        computer_score = computer_score + 1
        print("\nYour score ",user_score)
        print("The computer score ",computer_score)
    
    elif user == "Paper" and computer == "Rocks":
        print("\nThe user wins")
        user_score = user_score + 1
        print("\nYour score ",user_score)
        print("The computer score ",computer_score)
    
    elif user == computer:
        print("\nTie.")
        print("\nYour score ",user_score)
        print("The computer score ",computer_score)

print("\n Paper Scissors Game")
while(True):
    print("1.Rocks 2.Paper 3.Scissors")
    user = int(input("\nEnter the choice "))
    computer = l1[random.randrange(len(l1))]

    print("\nYour input ",l1[user-1])
    print("Computer input ",computer)
    winner(l1[user-1],computer)

    choice = input("\nDo you want to continue(Y/N)")
    if (choice == "N"):
        print("Program ended.")
        break




    


