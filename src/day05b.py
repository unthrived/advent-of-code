from utils import read_input
import numpy as np
import scipy as sp
data = read_input(day=5)

n = len(data)
nums = [str(i) for i in range(0, 10)]+['']
blanks = []

initial_seeds = data[0].split(': ')[1].split(' ')
# initial_seeds = int(initial_seeds)
for i in range(len(initial_seeds)):
    initial_seeds[i] = int(initial_seeds[i])
next = [0]*len(initial_seeds)
print(initial_seeds)

# seed = []
# soil = []
# fert = []
# water = []
# light = []
# temp = []
# humid = []
# loc = []

print(nums)
for i in range(n):
    if data[i]=='': blanks.append(i)
blanks.append(n)
highest = 0
for i in range(1,n):
    if i not in blanks:
        if i-1 not in blanks:
            data[i] = data[i].split(' ')
            for j in range(len(data[i])):
                data[i][j] = int(data[i][j])
                if data[i][j] > highest:
                    highest = data[i][j]

for k in range(
    len(initial_seeds)
    ):
    for j in range(len(blanks)-1):
        for i in range(blanks[j]+3, blanks[j+1]):
            # print(data[i-3])
            substraction = initial_seeds[k] - data[i][1]
            if 0 < substraction < data[i][2]: 
                next[k] = data[i][0] + substraction
                print(initial_seeds[k], data[i], next[k])
        initial_seeds[k] = next[k]

lowest = highest
for k in range(len(initial_seeds)):
    if initial_seeds[k] < lowest: lowest = initial_seeds[k]

seedss = np.zeros(highest)

print(lowest)