# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

inp = input("Enter a string of letters: ")

# if all(inp[i] == inp[len(inp) - (i+1)] for i in range(int(len(inp)/2))):
# int - to round the length of string, divide by two because you only need to check one way
if all(inp[i] == inp[len(inp) - (i+1)] for i in range(len(inp))):
    print('True')
else:
    print('False')

# BETTER SOLUTION

reverse = inp[::-1]
if inp == reverse:
    print('True')
else:
    print('False')