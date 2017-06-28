a = [7,8,5,4,9,2,5,5,10,3,1]

for i in range(1, len(a)):

    # loop starts at 1 because 0-1 = -1, and would cause an Index Error
    # the list is reversed so that the algorithm would start comparing from the last item
    for j in range(1, i + 1)[::-1]:
        # print(str(j) + "\n")

        # Here's how this works
        # For example we start with 1 3 2 8
        # Then we start comparing three and 2
        # The current index is "2", or i = 2
        # from the "j" loop, create a loop that counts 3 - 2 - 1, comparing each

        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]

print(a)