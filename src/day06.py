from utils import read_input
data = read_input(day=6)

n = len(data)

for i in range(n): 
    data[i] = data[i].split(':')[1]
    data[i] = data[i].split(' ')
    new_data = []
    for j in range(len(data[i])):
        if data[i][j] != '':
            new_data.append(int(data[i][j]))
    data[i] = new_data
print(data)

m = len(data[0])

prod = 1
for j in range(m):
    odd = 0
    beat = 0
    time = data[0][j]
    if time % 2: # odd
        odd = 1
    half = time // 2
    for k in range(half+1):
        
        dist = k * time
        time = time - 1
        if dist > data[1][j]: 
            beat += 1
        print(k, dist, beat)
    beat = beat * 2 + odd - 1
    prod = prod * beat

print(prod)
        
