
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