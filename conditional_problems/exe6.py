distance=int(input('Enter distance:'))

if distance<=3:
    print('Walk and enjoy')
elif distance>3 and distance<=15:
    print('Go with Bike')
elif distance>15:
    print('Go with car')
