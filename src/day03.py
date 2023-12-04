from utils import read_input
data = read_input(day=3)

n, m = len(data), len(data[0])
nums = [str(i) for i in range(0, 10)]
allowed = nums + ['.']
# print(allowed)
Mat_allowed = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if data[i][j] not in allowed:
            Mat_allowed[i][j] = 1
            if i != 0:
                Mat_allowed[i-1][j] = 1
            if j != 0:
                Mat_allowed[i][j-1] = 1
            if i != n-1:
                Mat_allowed[i+1][j] = 1
            if j != m-1:
                Mat_allowed[i][j+1] = 1
            
            if i != 0 and j != 0:
                Mat_allowed[i-1][j-1] = 1
            if i != n-1 and j != m-1:
                Mat_allowed[i+1][j+1] = 1
            if i != 0 and j != m-1:
                Mat_allowed[i-1][j+1] = 1
            if i != n-1 and j != 0:
                Mat_allowed[i+1][j-1] = 1
            # dont judge me please

for i in range(n): 
    print(Mat_allowed[i])

total = 0

for i in range(n):
    j = 0
    while j < m:
        number = 0
        add = False
        if data[i][j] in nums and j < m:
            while j < m and data[i][j] in nums:
                x = int(data[i][j])
                if Mat_allowed[i][j]: 
                    add = True
                    index = [i,j]
                number = number*10+x
                j = j+1
        j = j + 1
        # print(number, add)
        if add: 
            total = total + number
            print(number, index)
for i in range(n):
    print(Mat_allowed[i])

print(total)