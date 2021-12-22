import numpy as np

def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    return data

def main(path):
    data = read_data(path)

    solution = part1(data)
    solution2 = part2(data)
    print(solution)
    print(solution2)


def part1(data):
    sums = [0] * len(list(data[0]))

    for row in data:
        sums = np.add(sums, list(map(int, list(row))))

    gamma_bits = [1 if el > (len(data)/2) else 0 for el in sums]
    epsilon_bits = [1 if el == 0 else 0 for el in gamma_bits]

    gamma = int("".join(str(x) for x in gamma_bits), 2)
    epsilon = int("".join(str(x) for x in epsilon_bits), 2)
    
    return gamma*epsilon


def part2(data):

    binary_matrix = np.array([[int(digit) for digit in binary] for binary in data])
    oxygen = caculate_rating(binary_matrix, 0, 'max')
    c02 = caculate_rating(binary_matrix, 0, 'min')
    print(oxygen*c02)
        
def caculate_rating(data, index, setting):
    if len(data) == 1:
        rating = int("".join(str(x) for x in data[0]), 2)
        return rating

    zeros = []
    ones = []

    for row in data:
        if row[index] == 0:
            zeros.append(row)
        else:
            ones.append(row)

    if setting == 'max':
        bit_criteria = np.array(data.sum(axis=0) >= (len(data) / 2), dtype=int)
    else:
        bit_criteria = np.array(data.sum(axis=0) < (len(data) / 2), dtype=int)

    filtered_data = ones
    if bit_criteria[index] == 0:
        filtered_data = zeros

    index += 1
    return caculate_rating(np.array(filtered_data), index, setting)


if __name__ == "__main__":
    path = "input.txt"

    main(path)


