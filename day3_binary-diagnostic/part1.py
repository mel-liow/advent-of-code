import numpy as np

def main():

    with open("input.txt") as data:

        rows = data.read().splitlines()

        sums = [0] * len(list(rows[0]))

        for row in rows:
            sums = np.add(sums, list(map(int, list(row))))

        gamma_bits = [1 if el > (len(rows)/2) else 0 for el in sums]
        epsilon_bits = [1 if el == 0 else 0 for el in gamma_bits]

        gamma = int("".join(str(x) for x in gamma_bits), 2)
        episolon = int("".join(str(x) for x in epsilon_bits), 2)
        
        print(gamma*episolon)

if __name__ == "__main__":
    main()


