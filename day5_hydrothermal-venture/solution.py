import numpy as np
import re
from collections import defaultdict

def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    return data

def parse_data(data):

    coordinates = []

    for row in data:
        ints = [int(number) for number in re.split(",| -> ", row) if number.isdigit()]
        coordinates.append([(ints[0],ints[1]), (ints[2], ints[3])])

    return coordinates

def count_points(d):
    count = 0
    for i, val in d.items():
        for j, num in val.items():
            if d[i][j] >= 2:
                count += 1
    return count

def part1(data):
    
    d = defaultdict(lambda: defaultdict(int))

    for row in data:
        x1, y1 = row[0]
        x2, y2 = row[1]

        if x1 == x2:
            step = 1 if y1 < y2 else -1
            stop = y2+1 if y1 < y2 else y2-1
            for i in range(y1, stop, step):
                d[x1][i] += 1

        if y1 == y2:
            step = 1 if x1 < x2 else -1
            stop = x2+1 if x1 < x2 else x2-1
            for j in range(x1, stop, step):
                d[j][y1] += 1
    
    return count_points(d)
        

def main(path):
    raw_data = read_data(path)

    coordinates = parse_data(raw_data)
    solution1 = part1(coordinates)
    # solution2 = part2(random_numbers, boards)

    print(f'solution1: ', solution1),
    # print(f'solution2: ', solution2)
    

if __name__ == "__main__":
    path = "input.txt"

    main(path)


