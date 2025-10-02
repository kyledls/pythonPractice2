print("Welcome to Treasure Island. Your mission is to find the treasure.")
step_1 = input("\nleft or right? ")
if step_1 == "left":
    step_2 = input("swim or wait? ")
    if step_2 == "swim":
        print("game over")
    elif step_2 == "wait":
        step_3 = input("Which door? Red, Blue, or Yellow? ")
        if step_3 == "red":
            print("game over")
        elif step_3 == "blue":
            print("game over")
        elif step_3 == "yellow":
            print("You Win!")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
elif step_1 == "right":
    print("Game over")
else:
    print("Invalid input")