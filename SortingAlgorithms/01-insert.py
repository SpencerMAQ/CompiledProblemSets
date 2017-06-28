a = [7,8,5,4,9,2,5,5,10,3]

for i in range(len(a)):

    for j in range(1, i + 1)[::-1]:
        # print(str(j) + "\n")
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]

print(a)