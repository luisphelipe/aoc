import sys


def contains(a, b, x, y):
    return a >= x and b <= y or x >= a and y <= b


def solve(line):
    elf1, elf2 = line.split(',')
    a, b = [int(x) for x in elf1.split('-')]
    x, y = [int(x) for x in elf2.split('-')]
    return 1 if contains(a, b, x, y) else 0


def main():
    line = sys.stdin.readline()
    result = 0

    while line:
        result += solve(line)
        line = sys.stdin.readline()

    print(result)


main()
