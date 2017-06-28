# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.

# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89, 89, 89]

# basically checks every input of b if it exists in a
# filter(condition, list to check)
# common = list(filter(lambda b_item: b_item in a, b))
common = list(filter(lambda b_item: b_item in a, b))

# doesn't matter if a or b is the longer list

print(common)

# solution number 2
# solves for intersection by converting it first to a list
print(set.intersection(set(a),(b)))

# solution number 3


commons = []
def get_overlap(a, b):
    for i in range(max(len(a), len(b))):
        if len(a) >= len(b):
            # a[i] not in commons ensures that there are no duplicates in the commons list
            if (a[i] in b) and (a[i] not in commons):
                commons.append(a[i])

        elif len(b) > len(a):
            if (b[i] in a) and (b[i] not in commons):
                commons.append(b[i])

    print(commons)

get_overlap(a, b)

# for list in set:
# https://stackoverflow.com/questions/2541752/how-best-do-i-find-the-intersection-of-multiple-sets-in-python/2541814#2541814

# for nested lists:
# https://stackoverflow.com/questions/642763/find-intersection-of-two-lists