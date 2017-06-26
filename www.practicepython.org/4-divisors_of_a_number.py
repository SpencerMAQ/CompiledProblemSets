# Create a program that asks the user for a number and then prints out a
# list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides
# evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

while True:
    inp = input("Enter a number, type 'x' to quit: ")

    if inp == 'x':
        break

    else:
        # print(12%3)
        # from range 2 because 1 is always a divisor //  to inp+1 = inp itself
        list = [x for x in range(2, int(inp)+1) if int(inp)%x == 0]
        print(list)