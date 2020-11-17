print("Welcome to Tresure Island")
print("Your mission is to find the treasure")
choice1 = input("You're at the crossroad, where do you want to go? Type 'left' or 'right'. ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of it. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("The room was full of fire. Game Over.")
        elif choice3 == "blue":
            print("The room was full of water. Game Over.")
        elif choice3 == "yellow":
            print("The room was filled with shiny gold! You win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game over")

