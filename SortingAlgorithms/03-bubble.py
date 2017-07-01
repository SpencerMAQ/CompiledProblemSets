a = [100, 7, 8, 5, 4, 9, 2, 5, 5, 10, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2]


# stupid attempt
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

# 2nd attempt: works, but I forgot it's more efficient to use boolean operators
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
while not _sorted: # equiv = while _sorted == False:
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

# # solution by https://www.youtube.com/watch?v=YHm_4bVOe1s
# for i in range(len(a)-1):
#     for j in range(len(a) - 1 - i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)

# I have no idea why this works but I bet my logic-based solution works faster
