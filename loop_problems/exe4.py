# Reverse a string using a loop
input_string = input('Enter a String:')
reversed_str = ""

for char in input_string:
    reversed_str = char + reversed_str

print(reversed_str)