import numpy as np
from collections import defaultdict

days_new_fish_rest = 2
days_internal_cycle = 6
days_max_cycle = days_new_fish_rest + days_internal_cycle


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()
        input = [int(el) for el in data[0].split(',')]
    return input

def get_initial_state(data):
    
    initial_state = defaultdict(int)
    for i in range(days_max_cycle+1):
        initial_state[i] = data.count(i)

    return initial_state

def get_new_state(previous_state):
    days_max_cycle = 8
    
    state = defaultdict(int)
    for i in range(days_max_cycle+1):
        if i == days_max_cycle:
            state[i] = previous_state[0]
        elif i == 6:
            state[i] = previous_state[i+1] + previous_state[0]
        else:
            state[i] = previous_state[i+1]

    return state

def total_count(state):
    
    count = 0
    for key, vals in state.items():
        count += vals
    
    return count

def part1(data, days):
    
    for i in range(days+1):
        if i == 0:
            state = get_initial_state(data)
        else:
            previous_state = state
            state = get_new_state(previous_state)

    return total_count(state)

def main(path):
    data = read_data(path)

    solution1 = part1(data, 80)
    solution2 = part1(data, 256)

    print(f'solution1: ', solution1)
    print(f'solution2: ', solution2),

        

if __name__ == "__main__":
    path = "input.txt"

    main(path)


