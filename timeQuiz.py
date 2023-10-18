from random import randint

userTime = ''

while userTime != '0':
    hour = randint(0,24)
    minute = randint(1,60)
    militaryTime = f'{hour:0>2}{minute:0>2}'
    period = 'am' if hour < 12 else 'pm'
    if hour == 0:
        hour = 12
    hour = hour - 12 if hour > 12 else hour
    print(f"{hour}:{minute:0>2}{period}")

    correct = False
    while correct is False:
        userTime = input('Military Time (0 to exit): ') 
        if userTime == militaryTime:
            print('Correct')
            correct = True
        else:
            print('Incorrect')
