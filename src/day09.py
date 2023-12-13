from utils import read_input
data = read_input(day=9)

def result(sequence):
    print(sequence)
    total = 0
    for i in range(len(sequence)):
        for j in range(len(sequence)-i-1):
            sequence[j] = sequence[j+1] - sequence[j]
        print(sequence)
    for i in range(len(sequence)):
        total = total + sequence[i]
    
    print(total)
    return total

def previous(sequence):
    print(sequence)
    ls = []
    total = 0
    for i in range(len(sequence)):
        for j in range(len(sequence)-i-1):
            ls.append(sequence[0])
            sequence[j] = sequence[j+1] - sequence[j]
        print(ls)
    return total

n = len(data)

for i in range(n):
    data[i] = data[i].split(' ')
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

total = 0
for i in range(n):
    total = total + result(data[i])
print(total)
