def main():

    with open("input.txt") as data:
        rows = data.read().splitlines()

        rows_num = list(map(int, rows))
        count = 0
        
        for index, val in enumerate(rows_num):
            window_sum = sum(rows_num[index:index+3])
            window_sum_prev = sum(rows_num[index-1:index+2])

            if window_sum > window_sum_prev:
                count += 1

        print(count - 1)
    
if __name__ == "__main__":
    main()