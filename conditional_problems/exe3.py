score=int(input('Your soore please:'))
if score>=101:
    print('You can not get more than 100')
    exit()
if score>= 90:
    print('Your score is A')
elif score>= 80:
    print('Your score is B')
elif score>=70:
    print('Your score is C')
elif score>=60:
    print('Your score is D')
else:
    print('Your score is F')