from utils import read_input
data = read_input(day=1)

def part_one(data):
    ans = 0
    for i in range(len(data)):
        for j in range(0, len(data[i])):
            if ord(str(data[i][j])) in range(48,58):
                a = data[i][j]
                # print(a)
                break
        for j in reversed(range(0, len(data[i]))):
            if ord(str(data[i][j])) in range(48,58):
                b = data[i][j]
                # print(b)
                break
            
        a = int(a)
        b = int(b)
        add = 10*a+b
        print(i+1, add)
        ans = ans + add
    return ans

def part_two(data):
    numbers = [None]*9
    rnumbers = [None]*9
    letters = {1: 'one',
               2: 'two',
               3: 'three',
               4: 'four',
               5: 'five',
               6: 'six',
               7: 'seven',
               8: 'eight',
               9: 'nine'}

    rep = {1: '1e',
           2: '2o',
           3: '3e',
           4: '4r',
           5: '5e',
           6: '6x',
           7: '7n',
           8: '8t',
           9: '9e',

    }
    for i in range(len(data)):
        for j in range(1, 10):
            numbers[j-1] = data[i].find(letters[j])
            rnumbers[j-1] = data[i].rfind(letters[j])
        # print(numbers)
        if numbers == [-1]*9:
            pass
        else:
            lowest = 2000
            highest = -1
            for j in range(1, 10):
                if numbers[j-1] < lowest and numbers[j-1] != -1: 
                    lowest = numbers[j-1]
                    lowest_j = j
                if rnumbers[j-1] > highest: 
                    highest = rnumbers[j-1]
                    highest_j = j
        # print(lowest_j, highest_j)

            data[i] = data[i].replace(letters[lowest_j], rep[lowest_j], 1)
            data[i] = data[i].replace(letters[highest_j], rep[highest_j], 1)
            data[i] = data[i].replace(letters[lowest_j], rep[lowest_j])
            data[i] = data[i].replace(letters[highest_j], rep[highest_j])
        # print(i, lowest_j, highest_j, numbers)
    return data

#print(data)
data = part_two(data)
result = part_one(data)
print(result)