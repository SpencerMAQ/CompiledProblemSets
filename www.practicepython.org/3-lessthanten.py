# Take a list, say for example this one:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one,
# make a new list that has all the elements less than 5 from this list in
# it and print out this new list.
#
# Write this in one line of Python.
#
# Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.

# a = [round(x**1.2) for x in range(150) if round(x**1.2)%3==0]

import random as r

# nested list comprehension
rands = [x for x in [r.randint(0, 500) for i in range(1000)] if x%2 == 0]

less_than_five = [var for var in rands if var <= 5]

print(less_than_five)

## equivalent for loop
# for elem in rands:
#     if elem < 5:
#         less_than_five.append()
