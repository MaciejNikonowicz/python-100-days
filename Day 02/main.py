print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
how_many_people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = round(total_bill / how_many_people,2)

print(f"Each person should pay a total of ${bill_per_person}")
