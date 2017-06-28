# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
# Write this using at least one list comprehension.

import random as r

# list1 = r.sample(range(50), 20)
# list2 = r.sample(range(30), 15)

b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 89]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89, 89]

intersection = [i for i in set(a) if i in set(b)]

# or
# sorted(list(set([ element for element in a if element in b ])))
print(intersection)