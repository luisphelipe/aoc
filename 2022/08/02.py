import sys
import pprint
from functools import reduce

pp = pprint.PrettyPrinter(indent=4).pprint


def main():
    grid = []
    line = sys.stdin.readline()
    hidden = 0
    max_score = 0

    while line:
        grid.append([int(x) for x in list(line)[:-1]])
        line = sys.stdin.readline()

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            [scenic_score, is_hidden] = verify(grid, row, col)
            max_score = max(scenic_score, max_score)
            hidden += 1 if is_hidden else 0

    visible = len(grid) * len(grid[0]) - hidden

    print(f"there are {hidden} hidden trees")
    print(f"there are {visible} visible trees")
    print(f"maximum scenic score is {max_score}")


def verify(grid, row, col):
    value = grid[row][col]
    taller_than = []
    current_taller_than = 0
    count = 0

    # look up
    for i in range(row - 1, -1, -1):
        current = grid[i][col]
        current_taller_than += 1
        if (current >= value):
            count += 1
            break

    taller_than.append(current_taller_than)
    current_taller_than = 0

    # look down
    for i in range(row + 1, len(grid)):
        current = grid[i][col]
        current_taller_than += 1
        if (current >= value):
            count += 1
            break

    taller_than.append(current_taller_than)
    current_taller_than = 0

    # look left
    for i in range(col - 1, -1, -1):
        current = grid[row][i]
        current_taller_than += 1
        if (current >= value):
            count += 1
            break

    taller_than.append(current_taller_than)
    current_taller_than = 0

    # look right
    for i in range(col + 1, len(grid[0])):
        current = grid[row][i]
        current_taller_than += 1
        if (current >= value):
            count += 1
            break

    taller_than.append(current_taller_than)

    return [reduce(lambda a, b: a * b, taller_than), count == 4]


main()
