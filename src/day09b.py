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
        ls.append(sequence[0])
        for j in range(len(sequence)-i-1):
            sequence[j] = sequence[j+1] - sequence[j]
        print(ls)

    ls = ls[::-1]
    print(ls)
    for i in range(1, len(ls)):
        ls[i] = ls[i] - ls[i-1]
    print(ls)
    return ls[len(ls)-1]

n = len(data)

for i in range(n):
    data[i] = data[i].split(' ')
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

total = 0
for i in range(n):
    total = total + previous(data[i])
print(total)