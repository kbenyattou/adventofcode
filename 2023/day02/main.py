# Convert a string of drawn cubes into a dictionary of colour: number entries
def grab(grabstring):
    grabdict = {}
    grablist = grabstring.replace(',', '').split(' ')
    for i in range(int(len(grablist)/2)):
        grabdict[grablist[(2*i)+1]] = int(grablist[2*i])
    return grabdict

#12 red cubes, 13 green cubes, and 14 blue cubes
constraint = {
    'red':      12,
    'green':    13,
    'blue':     14
    }

maxtotal = sum(constraint.values())

# Checking that none of the colours exceed the constraint
def legit_grab(draw):
    return all([draw.get(colour, 0) <= constraint[colour] for colour in ['red', 'green', 'blue']])

with open('Desktop/input2.txt') as input:
    lines = input.read().split('\n')[:-1] # The last list is empty so sliced off

    numberofgames = 0
    powerofcubes = 0

    for line in lines:
        game_name, game_data = line.split(': ')
        game_id = game_name.split(' ')[1]
        draws = game_data.split('; ')
        for i in range(len(draws)):
            draws[i] = grab(draws[i])
        #print(draws)
        
        # Condition 1 is that the total cubes don't exceed maxtotal
        # Condition 2 is that each grab is valid (within the constraint)
        if all([ sum(draws[i].values()) <= maxtotal and legit_grab(draws[i]) for i in range(len(draws))]):
            numberofgames += int(game_id)

        power = 1
        for colour in ['red', 'green', 'blue']:
            power *= max([draw.get(colour, 0) for draw in draws])
        powerofcubes += power

    print(numberofgames)
    print(powerofcubes)
