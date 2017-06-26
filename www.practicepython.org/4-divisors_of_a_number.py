# Create a program that asks the user for a number and then prints out a
# list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides
# evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

__author__ = 'SpencerMAQ'

while True:
    inp = int(input("Enter a number, type '0' to quit: "))

    if inp == 0:
        break

    else:
        # print(12%3)
        # from range 2 because 1 is always a divisor //  to inp+1 = inp itself
        divisorList = [x for x in range(2, inp + 1) if inp%x == 0]
        print(divisorList)