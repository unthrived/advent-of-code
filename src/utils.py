def read_input(input_folder = 'input', day = 1):
    if day < 10:
        path = f'{input_folder}/day0{day}.txt'
    else:
        path = f'{input_folder}/day{day}.txt'
    print(f'Reading the input file of day {day} ...')
    with open(path, 'r') as f:
        data = f.readlines()
        data = list(map(str.strip, data))
    return data

