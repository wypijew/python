
name1 = input("What's your name? \n")
name2 = input("What's your partner's name? \n")

print("The Love Calculator is calculating your score...")

'''FIRST VERSION 
name1 = name1.lower()
name2 = name2.lower()

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')

total1 = str(t+r+u+e)
#print(total1)
l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e = name1.count('e') + name2.count('e')

total2 = str(l+o+v+e) 
#print(total2)
total = total1 + total2
#print(total)

total = int(total)

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total < 50 and total > 40:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")'''

#SECOND VERSION

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

''' Instructions:
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.

2. Check for the number of times the letters in the word LOVE occurs.

3. Combine these numbers to make a 2 digit number.

4. For Love Scores less than 10 or greater than 90, the message should be:
  "Your score is *x*, you go together like coke and mentos."

  5. For Love Scores between 40 and 50, the message should be:
  "Your score is *y*, you are alright together."

6. Otherwise, the message will just be their score. e.g.:
  "Your score is *z*."
'''