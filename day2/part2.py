def main():

    with open("input.txt") as data:

        rows = process_input(data)

        x = 0
        y = 0
        aim = 0

        for row in rows:
            direction, size = row
            if direction == "up":
                aim -= int(size)
            elif direction == "down":
                aim += int(size)
            elif direction == "forward":
                x += int(size)
                y += int(size) * aim


        print(f'x, y', (x, y))
        print(x*y)

def process_input(data):
    rows = data.read().splitlines()
    processed_data = list(map(lambda x: tuple(x.split()), rows))
    return processed_data
    
    
if __name__ == "__main__":
    main()


