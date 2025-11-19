coffee_size= str(input('Enter coffee size:')).lower()
extra_shot= str(input('Do you want extra shot?')).lower()

if coffee_size == 'small' and extra_shot =='yes':
    print(f'''Your {coffee_size} comes with an extra shot''')
elif coffee_size == 'small' and extra_shot == 'no':
    print(f'''Your {coffee_size} do not comes with an extra shot''')
elif coffee_size == 'medium' and extra_shot == 'yes':
    print(f'''Your {coffee_size} comes with an extra shot''')
elif coffee_size == 'medium' and extra_shot== 'no':
    print(f'''Your {coffee_size} do not comes with an extra shot''')
elif coffee_size == 'large' and extra_shot == 'yes':
    print(f'''Your {coffee_size} comes with an extra shot''')
elif coffee_size == 'large' and extra_shot == 'no':
    print(f'''Your {coffee_size} do not comes with an extra shot''')
else:
    print(f'''Your {coffee_size} is not in the list, please select any other coffee_size''')