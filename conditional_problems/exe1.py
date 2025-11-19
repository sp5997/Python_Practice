age= input('take user age:')
if int(age)<13:
    print('Your are a Minor')
elif int(age)>13 and int(age)<20:
    print('You are a Teenager')
elif int(age)<= 60:
    print('You are an Adult')
else:
    print('You are a Senior Citizen')
    