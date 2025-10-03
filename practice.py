import random

random_number = random.randint(0,2)
guess_counter = 3
print(random_number)
guessed_correct = False
difficulty_level = input("Choose difficulty. Easy or Hard").lower()
if difficulty_level == "easy":
    guess_counter = 10
elif difficulty_level == "hard":
    guess_counter = 3
else:
    print("invalid input")
while guessed_correct == False and guess_counter > 0:
    print(f"Lives remaining: {guess_counter}")
    user_guess = int(input("Guess the number "))
    if user_guess == random_number:
        print("You guessed right! You win!")
        guessed_correct = True
    elif user_guess > random_number:
        guess_counter -= 1
        print("You guessed too high")
    elif user_guess < random_number:
        guess_counter -= 1
        print("You guessed too low")
if guessed_correct == False:
    print(f"Out of guesses! The number was {random_number}")
reset_game = input("Do you want to play again")



    

