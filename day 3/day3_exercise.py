# Odd or even?
number = int(input("Enter a number: \n"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# elif, nested if
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age?"))
  if age < 12:
    bill += 5
    # Without defining the variable 'bill' in each condition, when the option 'no photo' is chosen the total bill will be 0.
    print("Child tickets are 5£.")
  elif age <= 18:
    bill += 7
    print("Youth tickets are 7£.")
  elif age >= 45 and age <= 55:
    bill = 0
    print("You're allowed to have a free ride!")
  else:
    bill += 12
    print("Adult tickets are 12£.")
    
  photo = input("Do you want a photo taken? Y or N. \n")
  if photo == "Y":
    bill += 3
  # Indentation of 'print' statement - the statement will be printed regardless of the selected photo option.
  print(f"Your total bill is {bill}£.")
else:
  print("Sorry, you have to grow taller before you can ride.")