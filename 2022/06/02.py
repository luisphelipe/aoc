import sys


def main():
    line = sys.stdin.readline()
    result = 0

    while line:
        result += solve(line)
        line = sys.stdin.readline()

    print(result)


def solve(line):
    for i in range(14, len(line)):
        queue = line[i-14:i]
        if has_only_unique(queue):
            return i


def has_only_unique(arr):
    return len(set(arr)) == 14


main()
