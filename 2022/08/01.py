import sys
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint


def main():
    grid = []
    line = sys.stdin.readline()
    result = 0

    while line:
        grid.append([int(x) for x in list(line)[:-1]])
        line = sys.stdin.readline()

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            result += verify(grid, row, col)

    hidden = result
    visible = len(grid) * len(grid[0]) - hidden

    print(f"there are {hidden} hidden trees")
    print(f"there are {visible} visible trees")


def verify(grid, row, col):
    value = grid[row][col]
    count = 0

    # look up
    for i in range(row - 1, -1, -1):
        current = grid[i][col]
        if (current >= value):
            count += 1
            break

    # look down
    for i in range(row + 1, len(grid)):
        current = grid[i][col]
        if (current >= value):
            count += 1
            break

    # look left
    for i in range(col - 1, -1, -1):
        current = grid[row][i]
        if (current >= value):
            count += 1
            break

    # look right
    for i in range(col + 1, len(grid[0])):
        current = grid[row][i]
        if (current >= value):
            count += 1
            break

    return 1 if count == 4 else 0


main()
