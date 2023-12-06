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
while k < len(initial_seeds):
    seed = initial_seeds[k]
    rang = initial_seeds[k+1]
    for j in range(len(blanks)-1): # iterate from seed-soil-fert-water etc 
        # print('j', j)
        # print(initial_seeds, 'j', j)
        for i in range(blanks[j]+2, blanks[j+1]): # we need to iterate for each seed-soil etc
            # print(data[i][0], data[i][1], data[i][2])
            print('i', i)
            substraction = initial_seeds[k] - data[i][1]
            # print('subs', substraction)
            if 0 <= substraction < data[i][2]:
                # if j==6:
                # print(i, k, data[i][0], data[i][1], data[i][2])
                overext = substraction + initial_seeds[k+1]
                if overext > data[i][2]:
                    #print('hi')
                    initial_seeds[k+1] = data[i][2] - substraction
                    initial_seeds[k] = data[i][0] + substraction
                    if k == 30: print('alert', initial_seeds[k+1])
                    initial_seeds.append(seed+initial_seeds[k+1])
                    initial_seeds.append(rang-initial_seeds[k+1])
                    rang = initial_seeds[k+1]
                    break
                else:
                    initial_seeds[k] = data[i][0] + substraction
                    break
        print(initial_seeds, 'j', j)
    k = k + 2
lowest = highest

for i in range(0, len(initial_seeds), 2):
    print(i, initial_seeds[i], initial_seeds[i+1])
    pass

for k in range(0, len(initial_seeds), 2):
    if initial_seeds[k] < lowest: 
        lowest = initial_seeds[k]
        print(lowest)

print(len(initial_seeds))
print(lowest)

sum = 0
for k in range(1, len(initial_seeds), 2):
    sum = sum + initial_seeds[k]
print('sum', sum)

# 21526469 ?????? last
# 22635950 too low
# 222541566
# 25430293
# 97802093
# 4294798436 too high
# 502964497
# 157103740
# 58485637
# 37809646
# 32956608 wrong
# 32956608
# 133060383 i dont know man
