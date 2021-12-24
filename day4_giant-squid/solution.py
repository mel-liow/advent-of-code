import numpy as np

def read_data(path):
    with open(path, "r") as f:
        lines = (line.rstrip() for line in f) 
        data = list(line for line in lines if line)

    return data

def parse_data(data):
    random_numbers = list(map(int, data.pop(0).split(',') ))
    boards = {}

    matrix_size = 5
    index = 0

    for n in range(0, len(data), matrix_size):
        matrix_list = data[n:n+matrix_size]
        numbers_list = []
        for row in matrix_list:
            numbers_list.append(list(map(int, list(filter(None, row.split(' '))))))
        
        boards[index] = np.array([numbers for numbers in numbers_list])
        index += 1

    return random_numbers, boards

def find_value(number, board):
    return np.where(board == number, np.nan, board)

def check_bingo(board):
    rows = np.nansum(board, axis=1)
    cols = np.nansum(board, axis=0)
    return np.any(rows == 0) or np.any(cols == 0)


def part1(random_numbers, boards):
    for i in random_numbers:
        for key in list(boards):
            boards[key] = find_value(i, boards[key])
            if check_bingo(boards[key]):
                sum = np.nansum(boards[key])
                return i*sum


def part2(random_numbers, boards):
    for i in random_numbers:
        for key in list(boards):
            boards[key] = find_value(i, boards[key])
            if check_bingo(boards[key]):
                sum = np.nansum(boards[key])
                if len(boards.keys()) == 1:
                    return i*sum
                
                del boards[key]


def main(path):
    raw_data = read_data(path)

    random_numbers, boards = parse_data(raw_data)
    solution1 = part1(random_numbers, boards)
    solution2 = part2(random_numbers, boards)

    print(f'solution1: ', solution1),
    print(f'solution2: ', solution2)
    

if __name__ == "__main__":
    path = "input.txt"

    main(path)


