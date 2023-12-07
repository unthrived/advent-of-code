from utils import read_input
data = read_input(day=7)

test = '3<456'
def poker(string):
    count = [0]*15
    for i in range(len(string)):
        j = ord(string[i])-48
        count[j] += 1
    if 5 in count:
        return 6
    if 4 in count:
        return 5
    if 3 in count and 2 in count:
        return 4
    if 3 in count:
        return 3
    if 2 not in count:
        return 0
    if 2 in count:
        count.remove(2)
        if 2 in count:
            return 2
    return 1

n = len(data)
for i in range(n): 
    data[i] = data[i].split(' ')
    data[i][0] = data[i][0].replace('T', ':')
    data[i][0] = data[i][0].replace('J', ';')
    data[i][0] = data[i][0].replace('Q', '<')
    data[i][0] = data[i][0].replace('K', '=')
    data[i][0] = data[i][0].replace('A', '>')
    data[i].append(poker(data[i][0]))

data.sort()
order = 1
for k in range(7):
    for i in range(n):
        if data[i][2] == k:
            data[i].append(order)
            order = order+1

for i in range(n):
    print(data[i])

total = 0
for i in range(746):
    print(data[i])
for i in range(n):
    total += int(data[i][1]) * data[i][3]


print(total)