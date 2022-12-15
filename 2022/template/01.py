import sys
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint


def main():
    line = sys.stdin.readline()
    result = 0

    while line:
        result += solve(line)
        line = sys.stdin.readline()

    print(result)


def solve(line):
    return len(line)


main()
