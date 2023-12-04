from utils import read_input
data = read_input(day=4)

n = len(data)
total_points = 0
amount_cards = [1 for i in range(n+10)]
total_cards = 0
for i in range(n):
    points = 0
    data[i] = data[i].split(': ')[1]
    data[i] = data[i].split(' | ')
    winning = data[i][0].split(' ')
    winning = [int(winning[i]) for i in range(len(winning)) if winning[i] !='']
    drawn = data[i][1].split(' ')
    drawn = [int(drawn[i]) for i in range(len(drawn)) if drawn[i] !='']
    for j in drawn:
        if j in winning: 
            points = points + 1
    # part one
    if points:
        total_points = total_points + pow(2, points-1)

    # part two
    for j in range(i+1, i+points+1):
        amount_cards[j] += amount_cards[i]

print('Part one: ', total_points)
for i in range(n):
    total_cards += amount_cards[i]
print('Part two: ', total_cards)