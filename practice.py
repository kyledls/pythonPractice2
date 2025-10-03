import random

user_is_finished = False
while user_is_finished == False:
    random_number = random.randint(0,2)
    total_wins = 0
    guess_counter = 10
    print(random_number)
    guessed_correct = False
    difficulty_level = input("Choose difficulty. Easy or Hard: ").lower()
    if difficulty_level == "easy":
        guess_counter = 10
    elif difficulty_level == "hard":
        guess_counter = 3
    else:
        print("invalid input")
    while guessed_correct == False and guess_counter > 0:
        print(f"Lives remaining: {guess_counter}")
        user_guess = int(input("Guess the number: "))
        if user_guess == random_number:
            total_wins += 1
            if total_wins == 1:
                print(f"You guessed right! You win! You have {total_wins} total win!")
            else:
                print(f"You guessed right! You win! You have {total_wins} total wins!")
            guessed_correct = True
        elif user_guess > random_number:
            guess_counter -= 1
            print("You guessed too high")
        elif user_guess < random_number:
            guess_counter -= 1
            print("You guessed too low")
    if guessed_correct == False:
        print(f"Out of guesses! The number was {random_number}")
    reset_game = input("Do you want to play again? Yes or No? ").lower()
    if reset_game == "yes":
        user_is_finished = False 
    elif reset_game == "no":
        print("Goodbye")
        user_is_finished = True




    

