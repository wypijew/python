line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? \n")

letter = position[0].lower()
abc = ['a', 'b', 'c']

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index] [letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")

'''
Write a program that will mark a spot on a map with an X.

Write a program that allows you to mark a square on the map using a letter-number system.

So an input of A3 should place an X at the position shown below:

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']

Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:
list = [['A', 'B, 'C'], 'E', 'F', 'G']
E is list[1] C is list[0][2]

'''