a = [7, 8, 5, 4, 9, 2, 5, 5, 10, 3, 1]

# ctr = 0
# for i in range(len(a)-1):
#     ctr = 0
#     while _sorted == False:
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
#             ctr += 1
#
#             if ctr > 0:
#                 _sorted = False
#             else:
#                 _sorted = True
#
# print(a)

# a = [7, 8, 5, 4, 9, 2]

# sorted_list=['True','True','True']
# print(all(['True','True','True']) == 'True')


# while True:
#     sorted_list = []
#
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
#             sorted_list.append(False)
#
#         else:
#             sorted_list.append(True)
#
#     if all([i == True for i in sorted_list]):
#         break
#
# print(a)

_sorted = False
while _sorted == False:
    _sorted = True

    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            # The way boolean logic is like this:
            # True and False = False
            # i.e. as long as any exchange is made, _sorted is set to false
            # _sorted = False iff there isn't a single exchange made
            _sorted = _sorted and False

        else:
            # if _sorted was previously 'False'
            # this boolean expression would still result to 'True'
            _sorted = _sorted and True

print(a)