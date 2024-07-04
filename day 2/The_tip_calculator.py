#Write a program that calculates how big is the share of the bill for each person based on user inputs.

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? \n£"))

tip = float(input("How much tip would you like to give? \n%"))

people = int(input("How many people to split the bill? \n"))

tip = tip / 100

the_share = (bill + bill * tip) / people

# the_share_rounded = round(the_share, 2) not always rounded the result to two decimal places 
the_share_rounded = "{:.2f}".format(the_share)

print(f"Each person should pay £{the_share_rounded}")