import sys
import pprint

sys.setrecursionlimit(9999)

pp = pprint.PrettyPrinter(indent=4).pprint

visited = {}


def main():
    grid = buildGrid()
    starting = getStartingPoint(grid)
    print("starting at", starting)
    result = solve(grid, starting, 0)
    print('final result is', result)


def buildGrid():
    grid = []
    line = sys.stdin.readline()[:-1]
    while line:
        grid.append(list(line))
        line = sys.stdin.readline()[:-1]
    return grid


def getStartingPoint(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                return [row, col]


def solve(grid, position, current):
    visited[tuple(position)] = [current]

    row, col = position
    cell = grid[row][col]

    if cell == 'E':
        #  print(current)
        return current

    neighbors = getNeighbors(position, len(grid), len(grid[0]))
    neighbors = filterInvalid(grid, neighbors, cell)
    neighbors = filterVisited(neighbors, visited, current + 1)

    if len(neighbors) == 0:
        return False

    solutions = []

    for neighbor in neighbors:
        sol = solve(grid, neighbor, current + 1)

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
        if neighbor == "E":
            neighbor = 'z'
        if ord(neighbor) <= (ord(value) + 1) or value == 'S':
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
