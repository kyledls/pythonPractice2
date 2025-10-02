import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")
computer_choice = random.randint(0, 2)

if user_choice == "0":
    if computer_choice == 0:
        print("Computer chose Rock\nYou tie.")
    elif computer_choice == 1:
        print("Computer chose Paper\nYou lose.")
    elif computer_choice == 2:
        print("Computer chose Scissors\nYou win.")

else:
    print("Invalid Input")
    
