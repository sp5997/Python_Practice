# Counting positive numbers
# numbers = [1,2,3,44,5,5,6,7,8]

Numbers = list(map(int, input('Enter numbers separated by spaces: ').split()))
positive_number = 0 
for num in Numbers:
       
    if num > 0:
        positive_number += 1
print(positive_number)

    