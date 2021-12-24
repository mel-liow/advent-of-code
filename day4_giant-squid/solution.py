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


def main(path):
    raw_data = read_data(path)

    random_numbers, boards = parse_data(raw_data)

    for i in random_numbers:
        for key, board in boards.items():
            boards[key] = find_value(i, board)
            if check_bingo(boards[key]):
                sum = np.nansum(boards[key])
                print(f'score:', i*sum)
                return

if __name__ == "__main__":
    path = "input.txt"

    main(path)


