
# 1st input: enter height in meters e.g: 1.65
height = float(input("Please, enter your height in meters: \n"))
# 2nd input: enter weight in kilograms e.g: 72.5
weight = float(input("Please, enter your weight in kilograms: \n"))

bmi_index = int((weight) / (height*height))

print(f"Your BMI index is {bmi_index}.")
