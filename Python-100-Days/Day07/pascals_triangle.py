def main():
    num = int(input('Number of rows:'))

    pascal_tri = [[]] * num

    for row in range(len(pascal_tri)):
        pascal_tri[row] = [None] * (row + 1)

        for col in range(len(pascal_tri[row])):
            if col == 0 or col == row:
                pascal_tri[row][col] = 1
            else:
                pascal_tri[row][col] = pascal_tri[row - 1][col] + pascal_tri[row - 1][col - 1]
            print(pascal_tri[row][col], end = '\t')
        print()

if __name__ == '__main__':
    main()
