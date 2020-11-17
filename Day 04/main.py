import random
import my_module

choices = {
    0: my_module.rock,
    1: my_module.paper,
    2: my_module.scissors
}

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)

print(user_choice)
print(choices[user_choice])
print(computer_choice)
print(choices[computer_choice])

if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
elif user_choice == computer_choice:
    print("It's a tie!")
else:
    print("You lose!")