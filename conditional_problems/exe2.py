age= int(input('enter your age:'))
day= str(input('enter the day:'))

price=0

if age>18 and day == 'wednesday':
    price= 12-2
    print('Your ticket price is:$', price)
elif age<18 and day== 'wednesday':
    price= 8-2
    print('Your tickett price is:$', price)
elif age> 18 and day!= 'wednesday':
    price=12
    print('Your ticket price is:$', price)
elif age<18 and day!= 'wednesday':
    price=8
    print('Your ticekt price is: $', price)