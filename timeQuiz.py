from random import randint

userTime = ''

while userTime != '0':
    hour = randint(1,24)
    minute = randint(1,60)
    militaryTime = f'{hour:0>2}{minute:0>2}'

    print(f"{hour - 12 if hour > 12 else hour}:{minute:0>2}{'am' if hour <= 12 else 'pm'}")

    correct = False
    while correct is False:
        userTime = input('Military Time (0 to exit): ') 
        if userTime == militaryTime:
            print('Correct')
            correct = True
        else:
            print('Incorrect')
