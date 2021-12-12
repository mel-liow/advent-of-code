import numpy as np

def main():

    with open("input.txt") as data:

        rows = data.read().splitlines()

        sums = [0] * len(list(rows[0]))

        for row in rows:
            sums = np.add(sums, list(map(int, list(row))))

        print(sums)
        print(len(rows)/2)

        answer = [1 if el > (len(rows)/2) else 0 for el in sums]
        print(answer)
        res = int("".join(str(x) for x in answer), 2)
        print(res)

if __name__ == "__main__":
    main()


