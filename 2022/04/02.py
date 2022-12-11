import sys


def overlaps(a, b, x, y):
    return a <= y and b >= x or x <= b and y >= a


def solve(line):
    elf1, elf2 = line.split(',')
    a, b = [int(x) for x in elf1.split('-')]
    x, y = [int(x) for x in elf2.split('-')]
    return 1 if overlaps(a, b, x, y) else 0


def main():
    line = sys.stdin.readline()
    result = 0

    while line:
        result += solve(line)
        line = sys.stdin.readline()

    print(result)


main()
