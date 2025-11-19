# Check if all elements in a list are unique, If a duplicate is found, exit the loop and print the duplicate
items = ['apple', 'apple', 'banana','mango']

duplicate = set()

for item in items:
    if item in duplicate:
        print("Duplicate:", item)
        break
    duplicate.add(item)