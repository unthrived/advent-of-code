from utils import read_input
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

current_map = 'AAA'
last_map = 'ZZZ'


for i in range(2, n):
    if data[i][0][2] == 'A': print(data[i][0])

print(current_map, last_map)

steps = 0
while current_map!=last_map:
    for j in range(len(data[0])):
        for i in range(2, n):
            if current_map == data[i][0]:
                if data[0][j] == 'L':
                    current_map = data[i][1][0]
                    break
                if data[0][j] == 'R': 
                    current_map = data[i][1][1]
                    break
        # print(j, current_map, steps)
        steps = steps + 1
print(steps)