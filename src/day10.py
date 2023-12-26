from utils import read_input
data = read_input(day=10)

n, m = len(data), len(data[0])
L = [[0 for _ in range(m)] for _ in range(n)]

print(n, m)

for i in range(n): 
    for j in range(m):
        if data[i][j] == '.':
            L[i][j] = 1 # here 1 means that is a point for part 2 purposes. 

def from_go(point, frm): 
    # I might think of a better way to do this
    if frm == 0:
        if point == 'L': go = 1
        if point == '|': go = 2
        if point == 'J': go = 3
    if frm == 1:
        if point == 'L': go = 0
        if point == '-': go = 3
        if point == 'F': go = 2
    if frm == 2:
        if point == '|': go = 0
        if point == 'F': go = 1
        if point == '7': go = 3
    if frm == 3:
        if point == 'J': go = 0
        if point == '-': go = 1
        if point == '7': go = 2
    return go

for i in range(n):
    for j in range(m):
        if data[i][j] == 'S': 
            start_i = i
            start_j = j
            L[i][j] = '*'

i, j = start_i, start_j - 1
frm = 1
steps = 0
while True:
    L[i][j] = 2
    go = from_go(data[i][j], frm)
    # 0 up
    # 1 right
    # 2 down
    # 3 left
    if go == 0: i = i - 1
    if go == 1: j = j + 1
    if go == 2: i = i + 1
    if go == 3: j = j - 1
    frm = (go + 2) % 4
    # print(start_i, start_j, i, j)
    steps = steps +1 
    if i==start_i and j==start_j: break
print(steps)

print((steps-1)/2)

def write_output():
    with open('src/day10_output.txt', 'w') as f:
        for i in range(n):
            for j in range(m):
                f.write(f'{L[i][j]}')
            f.write('\n')

# write_output()

