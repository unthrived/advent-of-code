from utils import read_input
data = read_input(day=3)

n, m = len(data), len(data[0])
nums = [str(i) for i in range(0, 10)]
allowed = nums + ['.']
allowed = ['*']
# print(allowed)
Mat_allowed = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if data[i][j] in allowed:
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



padding_allowed = [[0 for j in range(m+2)] for i in range(n+2)]
Mat_padding = [[0 for j in range(m+2)] for i in range(n+2)]

for i in range(n):
    for j in range(m):
        if data[i][j] in nums:
            Mat_padding[i+1][j+1] = 1

for i in range(n):
    for j in range(m):
        if data[i][j] == '*':
            if Mat_padding[i][j] and Mat_padding[i][j+1] and Mat_padding[i][j+2]:
                padding_allowed[i+1][j+1] = -1
            elif Mat_padding[i][j] and not Mat_padding[i][j+1] and Mat_padding[i][j+2]:
                padding_allowed[i+1][j+1] = -2
            elif not Mat_padding[i][j] and not Mat_padding[i][j+1] and not Mat_padding[i][j+2]:
                pass
            else: 
                padding_allowed[i+1][j+1] = -1

            if Mat_padding[i+2][j] and Mat_padding[i+2][j+1] and Mat_padding[i+2][j+2]:
                padding_allowed[i+1][j+1] -= 1
            elif Mat_padding[i+2][j] and not Mat_padding[i+2][j+1] and Mat_padding[i+2][j+2]:
                padding_allowed[i+1][j+1] -= 2
            elif not Mat_padding[i+2][j] and not Mat_padding[i+2][j+1] and not Mat_padding[i+2][j+2]:
                pass
            else: 
                padding_allowed[i+1][j+1] -= 1

            if Mat_padding[i+1][j]:
                padding_allowed[i+1][j+1] -= 1
            if Mat_padding[i+1][j+2]:
                padding_allowed[i+1][j+1] -= 1

for i in range(n+2):
    print(padding_allowed[i])

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
        if add: 
            print(number, index)
            padding_allowed[index[0]+1][index[1]+1] =  number

total_b = 0
for i in range (n+2):
    for j in range (n+2):
        if padding_allowed[i][j] == -2:
            values = [padding_allowed[i-1][j-1], 
                      padding_allowed[i-1][j],
                      padding_allowed[i-1][j+1],
                      padding_allowed[i][j-1],
                      padding_allowed[i][j+1],
                      padding_allowed[i+1][j-1],
                      padding_allowed[i+1][j],
                      padding_allowed[i+1][j+1]
                      ]
            prod = [value for value in values if value !=0]
            total_b = total_b + prod[0]*prod[1]

print(total_b)
