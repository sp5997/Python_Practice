# Find the first non repeated character
input_str = input('Enter your word:')

for char in input_str:
    if input_str.count(char) == 1:
        print(char)