from utils import read_input
data = read_input(day=6)

n = len(data)

for i in range(n): 
    data[i] = data[i].split(':')[1]
    data[i] = data[i].split(' ')
    new_data = ''
    for j in range(len(data[i])):
        if data[i][j] != '':
            new_data += data[i][j]
    new_data = int(new_data)
    data[i] = new_data
print(data)

def solve(data):
    odd = 0
    time = data[0]
    if time % 2: # odd
        odd = 1
    half = time // 2
    for k in range(half+1):
        dist = k * time
        time = time - 1
        if dist > data[1]: 
            return (half+1-k)*2+odd-1 # hehe maths

print(solve(data)) # 32607562
