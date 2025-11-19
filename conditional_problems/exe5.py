weather=(input('What is the weather today?')).lower()

if weather == 'sunny':
    print('Go for a walk')
elif weather == 'rainy':
    print('Read a book')
elif weather == 'snowy':
    print('Build a snowman')
else:
    print('This weather do not exists be at home quietly')