'''B IN THIS ONE STANDS FOR BRUTE FORCE!'''

from utils import read_input
data = read_input(day=5)

n = len(data)
nums = [str(i) for i in range(0, 10)]+['']
blanks = []

initial_seeds = data[0].split(': ')[1].split(' ')
# initial_seeds = int(initial_seeds)
for i in range(len(initial_seeds)):
    initial_seeds[i] = int(initial_seeds[i])
print(initial_seeds)

sum = 0
for k in range(1, len(initial_seeds), 2):
    sum = sum + initial_seeds[k]
print('sum', sum)

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

k = 0
m = len(blanks)
stop = True

print(initial_seeds)
k = 22635950 # brute forced
while True:
    value = k
    for j in range(m):
        
        for i in range(blanks[m-j-2]+2, blanks[m-j-1]):
            if data[i][0] <= value < data[i][0]+data[i][2]:
                value = data[i][1] + value - data[i][0]
                break
    print(k, value)
    for i in range(0, len(initial_seeds), 2):
        if initial_seeds[i] <= value < initial_seeds[i]+initial_seeds[i+1]:
            print('found', value)
            exit()
    k = k + 1
# while k < len(initial_seeds):
#     for j in range(len(blanks)-1): # iterate from seed-soil-fert-water etc 
#         for i in range(blanks[j]+2, blanks[j+1]): # we need to iterate for each seed-soil etc
#             pass

# 22635950 too low