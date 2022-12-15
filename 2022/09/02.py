import sys
import pprint
from math import copysign

pp = pprint.PrettyPrinter(indent=4).pprint


def main():
    line = sys.stdin.readline()[:-1]
    head = Head()
    tails = [Tail() for x in range(9)]

    while line:
        [direction, times] = line.split(" ")

        for i in range(int(times)):
            head.move(direction)
            tails[0].follow(head.coords)

            for i in range(1, 9):
                tails[i].follow(tails[i-1].coords, i == 8)

        line = sys.stdin.readline()[:-1]

    tail = tails[-1]
    #  pp(tail.visited)
    print("visited count:", len(tail.visited))
    unique = list(set(tail.visited))
    #  pp(unique)
    print("unique count:", len(unique))


class Coord:
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def coords(self):
        return {"x": self.x, "y": self.y}


class Head(Coord):
    def move(self, direction):
        dir_to_coord = {
            'R': [0, 1],
            'L': [0, -1],
            'U': [1, 0],
            'D': [-1, 0],
        }

        change = dir_to_coord[direction]
        self.x += change[0]
        self.y += change[1]


class Tail(Coord):
    def __init__(self):
        Coord.__init__(self)  # ugly
        self.visited = [
            (0, 0)
        ]

    def follow(self, coord, DEBUG=False):
        sc = self.coords

        diff_y = coord['y'] - sc['y']
        diff_x = coord['x'] - sc['x']

        follow_y = abs(diff_y)
        follow_x = abs(diff_x)

        if follow_y > 1 or follow_x > 1:
            if follow_y > 0 and follow_x > 0:
                self.y += int(copysign(1, diff_y))
                self.x += int(copysign(1, diff_x))

            elif follow_y > 1:
                self.y += int(copysign(1, diff_y))

            elif follow_x > 1:
                self.x += int(copysign(1, diff_x))

        #  DEBUG and print(self.coords)
        self.visited.append((self.x, self.y))


main()
