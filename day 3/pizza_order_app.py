print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f'Your total bill is {bill}£')

'''
Write an automatic pizza order program.
Based on a user's order, work out their final bill.

Small pizza (S): £15
Medium pizza (M): £20
Large pizza (L): £25

Add pepperoni for small pizza (Y or N): +£2
Add pepperoni for medium or large pizza (Y or N): +£3
Add extra cheese for any size pizza (Y or N): +£1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: £28.
'''