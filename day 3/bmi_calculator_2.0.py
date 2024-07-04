
# Enter your height in meters e.g., 1.55
height = float(input("Please, enter your height in meters: \n"))
# Enter your weight in kilograms e.g., 72.5
weight = float(input("Please, enter your weight in kilograms: \n"))

bmi_index = weight / (height*height)
bmi_index = round(bmi_index,2)

if bmi_index < 18.5:
  print(f"Your BMI is {bmi_index}, you are underweight.")
elif bmi_index < 25:
  print(f"Your BMI is {bmi_index}, you have a normal weight.")
elif bmi_index < 30:
  print(f"Your BMI is {bmi_index}, you are slightly overweight.")
elif bmi_index < 35:
  print(f"Your BMI is {bmi_index}, you are obese.")
else:
  print(f"Your BMI is {bmi_index}, you are clinically obese.")

'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

Important: you do not need to round the result to the nearest whole number. It's fine to print out a floating point number for this exercise. The interpretation message needs to include the words from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

Example Input 1
1.50
63
Example Output 1
Your BMI is 28.0, you are slightly overweight.
since 63 ÷ (1.50 x 1.50) = 28
'''
  