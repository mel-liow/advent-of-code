def main():

    with open("input.txt") as data:
        rows = data.read().splitlines()
        count = 0

        for index, val in enumerate(rows):
            if int(val) > int(rows[index-1]):
                count += 1

        print(count)
    
if __name__ == "__main__":
    main()
