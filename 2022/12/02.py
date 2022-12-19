import sys
import pprint

sys.setrecursionlimit(9999)

pp = pprint.PrettyPrinter(indent=4).pprint

visited = {}


def main():
    grid = buildGrid()
    starting = getStartingPoint(grid, 'E')
    print("starting at", starting)
    result = solve(grid, starting, 0, 'a')
    print('final result is', result)


def buildGrid():
    grid = []
    line = sys.stdin.readline()[:-1]
    while line:
        grid.append(list(line))
        line = sys.stdin.readline()[:-1]
    return grid


def getStartingPoint(grid, target):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == target:
                return [row, col]


def solve(grid, position, current, target):
    visited[tuple(position)] = [current]

    row, col = position
    cell = grid[row][col]

    if cell == target:
        print(current)
        return current

    neighbors = getNeighbors(position, len(grid), len(grid[0]))
    #  print('on get', neighbors)
    neighbors = filterInvalid(grid, neighbors, cell)
    #  print('on invalid', neighbors)
    neighbors = filterVisited(neighbors, visited, current + 1)
    #  print('on visited', neighbors)

    if len(neighbors) == 0:
        return False

    solutions = []

    for neighbor in neighbors:
        sol = solve(grid, neighbor, current + 1, target)

        if sol != False:
            solutions.append(sol)

    if len(solutions) == 0:
        return False

    return min(solutions)


def getNeighbors(position, height, width):
    row, col = position
    positions = []

    if (col < width - 1):
        positions.append([row, col + 1])
    if (row < height - 1):
        positions.append([row + 1, col])
    if (row > 0):
        positions.append([row - 1, col])
    if (col > 0):
        positions.append([row, col - 1])

    return positions


def filterInvalid(grid, positions, value):
    pos = []
    for position in positions:
        row, col = position
        neighbor = grid[row][col]
        if value == "E":
            value = 'z'
        if ord(neighbor) >= (ord(value) - 1):
            pos.append(position)
    return pos


def filterVisited(positions, visited, current):
    pos = []
    for position in positions:
        vis = visited.get(tuple(position), False)
        if not vis or current < vis[0]:
            pos.append(position)
    return pos


main()
