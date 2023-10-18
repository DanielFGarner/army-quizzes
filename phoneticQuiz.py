import random
import time

letterDict = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'xray',
    'y': 'yankee',
    'z': 'zulu'
}

incorrect = []

startTime = time.time()

while len(letterDict) > 0:
    letter, phonetic = random.choice(list(letterDict.items()))
    answer = str.lower(input(f'What is the phonetic word for {str.upper(letter)}? \nAnswer: '))

    if answer == phonetic:
        print('Correct')
        del letterDict[letter]
    else:
        print('Incorrect, the answer was ', str.capitalize(phonetic))
        if (letter, phonetic) not in incorrect:
            incorrect.append((letter, phonetic))

deltaTime = round(time.time() - startTime, 2)

if len(incorrect) > 0:
    print('The letters you got incorrect were', end=' ')
    for entry in incorrect:
        print(f'{str.upper(entry[0])}: {str.capitalize(entry[1])}  ', end=' ')

print(f'\nTotal Time: {deltaTime}s' )
