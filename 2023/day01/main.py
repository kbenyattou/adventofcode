import regex as re

# Keys for parts 1 and 2 of the problem
numberkeyone = '\d'
numberkeytwo = 'one|two|three|four|five|six|seven|eight|nine|\d'

# Takes a string, outputs the desired list of substrings
def retriever(line):
    return re.findall(numberkeytwo, line, overlapped=True)

numberdict = {
    'one':     '1',
    'two':     '2',
    'three':   '3',
    'four':    '4',
    'five':    '5',
    'six':     '6',
    'seven':   '7',
    'eight':   '8',
    'nine':    '9'
    }

def convertchar(entry):
    try:
        return numberdict[entry]
    except:
        return entry

def convertlist(testlist):
    return int(convertchar(testlist[0]) + convertchar(testlist[-1]))

with open('Desktop/input1.txt') as input:
    contents = input.read().split('\n')[:-1] # The last list is empty so sliced off
    sum = 0
    for i in range(len(contents)):
        sum += convertlist(retriever(contents[i]))
    print(sum)
