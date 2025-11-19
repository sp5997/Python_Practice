# compute factorial of a number using while loop
input_num = int(input('Enter your num:'))
factorial = 1
while input_num > 0:
    factorial = factorial * input_num
    input_num = input_num - 1

print(factorial)

