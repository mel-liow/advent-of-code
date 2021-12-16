import numpy as np

def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    return data

def main(path):
    data = read_data(path)

    solution = part1(data)
    print(solution)


def part1(data):

    sums = [0] * len(list(data[0]))

    for row in data:
        sums = np.add(sums, list(map(int, list(row))))

    gamma_bits = [1 if el > (len(data)/2) else 0 for el in sums]
    epsilon_bits = [1 if el == 0 else 0 for el in gamma_bits]

    gamma = int("".join(str(x) for x in gamma_bits), 2)
    epsilon = int("".join(str(x) for x in epsilon_bits), 2)
    
    return gamma*epsilon


if __name__ == "__main__":
    path = "input.txt"

    main(path)


