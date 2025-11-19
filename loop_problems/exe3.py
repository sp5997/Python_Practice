#Print the multiplication table for a given number, but skip the 5th iteration
number = int(input('Enter a number:'))

for i in range(1, 11):
    if i == 5:
        continue           # it detects the value 5 and skips it
    print(number * i)