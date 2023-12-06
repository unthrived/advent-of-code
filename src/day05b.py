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

# seed = []
# soil = []
# fert = []
# water = []
# light = []
# temp = []
# humid = []
# loc = []

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
for j in range(len(blanks)-1): # iterate from seed-soil-fert-water etc 
    print('j', j)
    
    for i in range(blanks[j]+2, blanks[j+1]): # we need to iterate for each seed-soil etc
        # print(data[i][0], data[i][1], data[i][2])
        # print('i', i)
        k = 0
        while k < len(initial_seeds):
            substraction = initial_seeds[k] - data[i][1]
            # print('subs', substraction)
            if 0 < substraction < data[i][2]:
                print(i, substraction, data[i][2], initial_seeds[k], data[i][1])
                overext = substraction + initial_seeds[k+1]
                if overext > data[i][2]:
                    
                    oldk1 = initial_seeds[k+1]
                    initial_seeds[k+1] = data[i][2] - substraction
                    initial_seeds.append(data[i][1]+data[i][2]) # append value
                    initial_seeds.append(initial_seeds[k+1]+substraction-data[i][2]) # append range
                    initial_seeds[k] = data[i][0] + substraction
                else:
                    initial_seeds[k] = data[i][0] + substraction

            k = k + 2
            # print(initial_seeds)
    # print('len', len(initial_seeds))
    #print('next', initial_seeds)

lowest = highest

print(initial_seeds)

for i in range(0, len(initial_seeds), 2):
    # print(initial_seeds[i], initial_seeds[i+1])
    pass

for k in range(0, len(initial_seeds), 2):
    if 0 < initial_seeds[k] < lowest: lowest = initial_seeds[k]

print(lowest)


# 22635950 too low
# 222541566
# 97802093
# 4294798436 too high