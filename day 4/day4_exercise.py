
import random

'''
Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important! The first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".

You should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

Example Output
Heads
or
Tails
'''
random_toss = random.randint(0,1)

if random_toss == 0:
    print("Tails")
else:
    print("Heads")


# names = names.string.split(", ")
#Generate random choice who is paying for the meal 

import random

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

print(f"{names[random_choice]} is going to buy the meal today!")
