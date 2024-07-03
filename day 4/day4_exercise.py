
import random

random_toss = random.randint(0,1)

if random_toss == 0:
    print("Tails")
else:
    print("Heads")


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)


# names = names.string.split(", ")

import random

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

print(f"{names[random_choice]} is going to buy the meal today!")

