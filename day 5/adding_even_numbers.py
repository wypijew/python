'''
Instructions
Write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important! There should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
30

'''

target = int(input("Enter a number between 0 and 1000: \n"))

sum = 0
for number in range(0, target + 1,2):
  sum += number

print(sum)

'''
OR

For odd numbers:

sum = 0
for number in range(1, target + 1):
   if number % 2 != 0:
    sum += number
print(sum)

'''