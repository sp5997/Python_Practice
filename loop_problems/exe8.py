# Check if a number is prime

input_num = int(input('Enter a number:'))
is_prime = True
if input_num  > 1:
    for i in range(2, input_num):
        if (input_num % i) == 0:
            is_prime = False
            break

print(is_prime)