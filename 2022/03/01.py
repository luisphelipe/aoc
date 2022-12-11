import sys


def char_value(char):
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1


def solve(line):
    left = {}

    middle_index = len(line)//2

    for char in line[:middle_index]:
        if (left.get(char, False)):
            left[char] += 1
        else:
            left[char] = 1

    for char in line[middle_index:]:
        if (left.get(char, False)):
            return char_value(char)


def main():
    line = sys.stdin.readline()
    result = 0

    while line:
        result += solve(line)
        line = sys.stdin.readline()

    print(result)


main()
