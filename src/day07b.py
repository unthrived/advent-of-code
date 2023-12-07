from utils import read_input
data = read_input(day=7)

def poker(string):
    count = [0]*15
    for i in range(len(string)):
        j = ord(string[i])-48 # ASCII '0' -> 0
        count[j] += 1
    jokers = count[1]
    count.pop(1)
    if 5 in count:
        return 6 + 10*jokers
    if 4 in count:
        return 5 + 10*jokers
    if 3 in count and 2 in count:
        return 4 + 10*jokers
    if 3 in count:
        return 3 + 10*jokers
    if 2 not in count:
        return 0 + 10*jokers
    if 2 in count:
        count.remove(2)
        if 2 in count:
            return 2 + 10*jokers
    return 1 + 10*jokers

# 0 nothing
# 1 pair
# 2 two pair
# 3 three kind
# 4 full h
# 5 poker
# 6 ace

def joker(a, b):
    if b == 0: return a
    if a == 2: return 4
    if a == 1:
        if b == 1: return 3
        if b == 2: return 5
        if b == 3: return 6
    if a == 4: return 6
    if a == 3: return a + b + 1
    if a == 0:
        if b == 1: return 1
        if b == 2: return 3
        if b == 3: return 5
        if b == 4 or b == 5: return 6
    if a == 5: return 6

n = len(data)
for i in range(n): 
    data[i] = data[i].split(' ')
    data[i][0] = data[i][0].replace('T', ':')
    data[i][0] = data[i][0].replace('J', '1')
    data[i][0] = data[i][0].replace('Q', '<')
    data[i][0] = data[i][0].replace('K', '=')
    data[i][0] = data[i][0].replace('A', '>')
    data[i].append(poker(data[i][0]))

data.sort()

order = 1
for k in range(7):
    for i in range(n):
        if data[i][2]%10 == k:
            data[i].append(order)
            data[i].append(data[i][2]//10)
            data[i][2] = data[i][2] % 10
            data[i].append(joker(data[i][2], data[i][4]))
            order = order+1

order = 1
for k in range(7):
    for i in range(n):
        if data[i][5] == k:
            data[i].append(order)
            order = order+1

total = 0
for i in range(n):
    total += int(data[i][1]) * data[i][6]

print(total) #248781813