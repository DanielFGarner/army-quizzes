import msvcrt

creedLines = ['I am an American Soldier.',
              'I am a warrior and a member of a team.',
              'I serve the people of the United States, and live the Army Values.',
              'I will always place the mission first.',
              'I will never accept defeat.',
              'I will never quit.',
              'I will never leave a fallen comrade.',
              'I am diciplined, physically and mentally tough, trained and proficient in my warrior tasks and drills.',
              'I always maintain my arms, my equipment, and myself.',
              'I am an expert and I am a professional.',
              'I stand ready to deploy, enage, and destroy the enemies of the United States of America in close combat.',
              'I am a guardian of freedom and the American way of life.',
              'I am an American Soldier.'
              ]

level = 0
mode = ''
modifier = ''

def Quiz(creed):
    userAnswer = ''
    while len(creed) > 0:
        userInput = str(msvcrt.getch())[2]

        if userInput == "\\":
            return True

        if userInput == creed[0]:
            userAnswer += userInput
            print(userAnswer)
            creed = creed[1:]

        else:
            print('Incorrect')

while mode != 'q':
    mode = input('Select Mode (r, w): ') # Select read or write mode
    modifier = input('Select Modifier (s, a, r): ') # select single, all, or range of lines

    if mode == 'w':
        if modifier == 's':
            level = int(input('Select Level (1-13): ')) - 1
            Quiz(creedLines[level])
        if modifier == 'a':
            for lvl in range(0, 13):
                if Quiz(creedLines[lvl]):
                    break
        if modifier == 'r':
            startLevel = int(input('Select Starting Level (1-13): ')) - 1
            for lvl in range(startLevel, 13):
                Quiz(creedLines[lvl])

    if mode == 'r':
        if modifier == 's':
            level = int(input('Select Level (1-13): ')) - 1
            print(f'{level + 1:2}: {creedLines[level]}')
        if modifier == 'a':
            for lvl in range(0,13):
                print(f'{lvl + 1:2}: {creedLines[lvl]}')
        if modifier == 'r':
            startLevel = int(input('Select Starting Level (1-13)')) - 1
            for lvl in range(startLevel, 13):
                print(f'{lvl + 1:2}: {creedLines[lvl]}')
