import sys
import pprint
from time import sleep

pp = pprint.PrettyPrinter(indent=4).pprint

AIR = '.'
ROCK = '#'
SAND = 'o'


def main():
    result = solve()
    print("result is", result)


def solve():
    (grid, leftmost) = build_grid()
    (grid, cont) = simulate_grain_of_sand(grid, leftmost)
    result = 0

    while cont:
        #  sleep(0.05)
        #  print_grid(grid)
        result += 1
        (grid, cont) = simulate_grain_of_sand(grid, leftmost)

    #  pp(grid)
    return result


def build_grid():
    dots = []
    line = sys.stdin.readline()
    while line:
        dots.extend(parse_line(line))
        line = sys.stdin.readline()

    (width, height, leftmost) = get_grid_dimensions(dots)
    #  print(f"width={width} and height={height}")
    grid = [[AIR] * width for x in range(height - 1)]
    grid.append([ROCK] * width)
    grid = fill_grid(grid, dots, leftmost)
    return (grid, leftmost)


def parse_line(line):
    points = []
    for coords in line.split(" -> "):
        coord = [int(x) for x in coords.split(",")]
        points.append(tuple(coord))
    #  print("points:", points)
    edges = [points[0]]
    for i in range(1, len(points)):
        edge = build_edges(points[i - 1], points[i])
        edges.extend(edge)
    #  print("edges:", edges)
    return edges


def build_edges(start, end):
    #  print(start, end)
    (x1, y1) = start
    (x2, y2) = end
    edges = []
    if x1 != x2:
        inc = sign(x2 - x1)
        x1 += inc
        while x2 + inc != x1:
            edges.append((x1, y1))
            x1 += inc
    elif y1 != y2:
        inc = sign(y2 - y1)
        y1 += inc
        while y2 + inc != y1:
            edges.append((x1, y1))
            y1 += inc
    return edges


def sign(x):
    return -1 if x < 0 else 1


def get_grid_dimensions(dots):
    bottom = dots[0]
    left = dots[0]
    right = dots[0]
    for dot in dots:
        if dot[1] > bottom[1]:
            bottom = dot
        if dot[0] < left[0]:
            left = dot
        if dot[0] > right[0]:
            right = dot
    height = bottom[1] + 3
    width = height * 2 - 1
    leftmost = 500 - height + 1
    return (width, height, leftmost)


def fill_grid(grid, dots, leftmost):
    for dot in dots:
        x = dot[1]
        y = dot[0] - leftmost
        grid[x][y] = ROCK
    return grid


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()


def simulate_grain_of_sand(grid, leftmost):
    x = 0
    y = 500 - leftmost

    if grid[x][y] is SAND:
        return (grid, False)

    while y >= 0 and y < len(grid[0]) and x < len(grid):
        try:
            if should_move_bottom(grid, x, y):
                pass
            elif should_move_left(grid, x, y):
                y -= 1
            elif should_move_right(grid, x, y):
                y += 1
            else:
                grid[x][y] = SAND
                return (grid, True)
            x += 1
        except:
            break

    return (grid, False)


def should_move_bottom(grid, x, y):
    return grid[x + 1][y] is AIR


def should_move_left(grid, x, y):
    return grid[x + 1][y - 1] is AIR


def should_move_right(grid, x, y):
    return grid[x + 1][y + 1] is AIR


main()
