# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

while True:
    inp = input("Enter an integer, type x to close: ")

    if inp == 'x':
        break

    elif int(inp)%2 == 0:
        print('number is even')

    elif int(inp)%2 != 0:
        print("number is odd")

    else:
        print('Please enter valid input')