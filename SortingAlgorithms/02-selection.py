a = [7, 8, 5, 4, 9, 2, 5, 5, 10, 3, 1]

# i = 4
#
# print(a[i])
# print(min(a[i+1:]))

# for i in range(len(a)+1):
#     print(i)
#     _min = min(a[i+1:])
#     index_of_min = a.index(_min)
#     current = a[i]
#     if current > _min:
#         current, a[index_of_min] = a[index_of_min], current
#
# print(a)
# min_val = a[0]

# a = [7, 8, 5, 4, 9, 2]


## doesn't work if the list has duplicates (if you use min_val)
## runs on O(n2)

## the reason min_index is better that min_val is because min_val keeps track of the
## index of the item even if there are duplicates
## unlike min_val wherein it takes the index of the first item (of the duplicates)

for i in range(len(a)-1):
    # min_val = a[i]
    min_index = i
    for j in range(i+1, len(a)):
        if a[min_index] > a[j]:
            # min_val = a[j]
            min_index = j
        # else:

            # assert isinstance(i, object)
            # min_val = a[i]

    # index_of_min = a.index(min_val)

    if min_index != i:  # just to save resources, you won't need to swap if they're the same
        a[i], a[min_index] = a[min_index], a[i]

print(a)
