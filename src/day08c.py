from utils import read_input
from math import lcm
data = read_input(day=8)

def to_numeral(string):
    numeral = 0
    n = len(string)
    for j in range(n):
        numeral += 26**(n-j-1)*ord(string[j])
    return numeral

n = len(data)
for i in range(2, n):
    data[i] = data[i].split(' = (')
    data[i][1] = data[i][1].split(')')[0]
    data[i][1] = data[i][1].split(', ')

# print(ord('A'), ord('Z'))

for i in range(2, n):
    numeral = to_numeral(data[i][0])
    data[i].append(numeral)
    data[i].append(to_numeral(data[i][1][0]))
    data[i].append(to_numeral(data[i][1][1]))

current_map = []

for i in range(2, n):
    if data[i][0][2] == 'A':
        current_map.append(data[i][0])
print(current_map)

def nmap(mapp, data, char):
    n = len(data)
    for i in range(2, n):
        if mapp == data[i][0]:
            if char == 'L':
                mapp = data[i][1][0]
                return mapp
            if char == 'R':
                mapp = data[i][1][1]
                return mapp

def isz (current_map):
    z = 0
    for k in range(len(current_map)):
        if current_map[k][2] == 'Z':
            z = z+1
    if z == len(current_map): return True
    else: return False


steps = 0
br = True

result_map = []

for z in range(len(current_map)):
    iter_map = [current_map[z]]
    while br:
        for j in range(len(data[0])):
            next_map = []
            #print(iter_map, steps, data[0][j])
            for k in range(len(iter_map)):
                next_map.append(nmap(iter_map[k], data, data[0][j]))
            iter_map = next_map
            #print(iter_map, steps, data[0][j])

            steps = steps + 1
            if isz(iter_map): br = False
    result_map.append(steps)

# 18113 59 307
# 20569 67 307
# 21797 71 307
# 13201 43 307
# 24253 79 307
# 22411 73 307

print(lcm(18113, 20569, 21797, 13201, 24253, 22411))