import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me all the names, separated by comma(,): ")
names = nameAsCSV.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
print(names[random_choice])
