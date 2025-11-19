# Keep asking the user for input until they enter a number between 1 and 10

while True:
    input_1 = int(input("Enter value bwtween 1 and 10:"))
    if 1 <= input_1 <= 10:
        print('Good')
        break
    else:
        print('Enter number in range of 1 to 10')