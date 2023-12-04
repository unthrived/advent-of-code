#from itertools import permutations as perm
from utils import read_input
data = read_input(day=2)

for i in range(len(data)):
    data[i] = data[i].split(': ')[1] # remove Game 1: '

def solve(part = 1):
    amount = 0 #part1
    total_prod = 0 #part2
    for i in range(len(data)): # GAME
        count = 1
        RBG_max = [0, 0, 0]
        cubes = data[i].split('; ')
        for j in range(len(cubes)):
            cube = cubes[j].split(', ')
            RBG = [cubes[j].find(' red'), cubes[j].find(' blue'), cubes[j].find(' green')]
            RBG_final = [None]*3
            for k in range(len(cube)):
                cube[k] = cube[k].replace(' red', '')
                cube[k] = cube[k].replace(' blue', '')
                cube[k] = cube[k].replace(' green', '')
                cube[k] = cube[k].replace('\n', '') # strip

            for x in range(len(cube)):
                cube[x] = int(cube[x])

            # CAN BE DONE MORE EFFICIENTLY WITH PERM MATRICES, SOONTM
            for z in range(3): 
                if RBG[z] == -1:
                    RBG_final[z] = 0
                elif RBG[z] in range(0, 3):
                    RBG_final[z] = cube[0]
                elif RBG[z] in range(8, 13):
                    RBG_final[z] = cube[1]
                elif RBG[z] in range(16, 21): 
                    RBG_final[z] = cube[2]

            # part one 2447
            for z in range(3):
                if RBG_final[0] > 12 or RBG_final[1] > 14 or RBG_final[2] > 13:
                    count = 0
                    break

            # part two 
            for z in range(3):
                if RBG_final[z] > RBG_max[z]: 
                    RBG_max[z] = RBG_final[z]
        prod = 1
        for z in range(3):
            prod = prod * RBG_max[z]

        if count: 
            id = i+1
            amount = amount + id
        
        total_prod = total_prod + prod
    if part == 1: return amount
    return total_prod

print('Part one: ', solve())
print('Part two: ', solve(part=2))

        # if -1 not in RBG:
        #     # print(RBG_sorted)
        #     perm = [
        #     RBG.index(RBG_sorted[0]), 
        #     RBG.index(RBG_sorted[1]), 
        #     RBG.index(RBG_sorted[2])]
        #     for permutation in range(3):
        #         RBG_final[permutation] = cube[perm[permutation]]
        #     # print(RBG_final, 'RBG')