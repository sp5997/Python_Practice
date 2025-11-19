# Pet food recommendation
# Recoomend food type for a pet based on pet's species and age
# Species - Dog Age <2 yrs Food - Puppy food
# Species - Cat Age >5yrs Food - Senior cat food

Species= input('Enter species of animal:')
Age= int(input('Enter age of animal:'))

if Species == 'dog' and (Age)<2:
    print('You need a puppy food')
elif Species == 'dog' and (Age)>2:
    print('You need a healthy dog food')
if Species == 'cat' and (Age)<2:
    print('You need a small cat food')
elif Species == 'cat' and (Age)>2:
    print('Give him senior cat food')