from itertools import permutations as perm

path = 'input/day02.txt'

with open(path, 'r') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].split(': ')[1] # remove Game 1: '

baseline = [12, 13, 14] # RGB

#for i in range(len(data)):
amount = 0
for i in range(
    #len(data)
    1
    ):
    cubes = data[i].split('; ')
    for j in range(len(cubes)):
        cube = cubes[j].split(', ')
        RBG = [cubes[j].find(' red'), cubes[j].find(' blue'), cubes[j].find(' green')]
        RBG_sorted = sorted(RBG)
        RBG_values = [None]*3
        for k in range(len(cube)):
            cube[k] = cube[k].replace(' red', '')
            cube[k] = cube[k].replace(' blue', '')
            cube[k] = cube[k].replace(' green', '')
            cube[k] = cube[k].replace('\n', '') # strip
        print(RBG, 'position')

        for x in range(len(cube)):
            cube[x] = int(cube[x])
        print(cube)

        # CAN BE DONE MORE EFFICIENT WITH PERM MATRICES, SOONTM

        print(RBG_sorted)
        print(RBG.find(RBG_sorted[0]))