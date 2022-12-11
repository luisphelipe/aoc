import sys


def char_value(char):
    if char.isupper():
        return ord(char) - ord('A') + 27
    return ord(char) - ord('a') + 1


def create_dict(line):
    tmp = {}

    for char in line:
        if char == "\n":
            break
        if not tmp.get(char):
            tmp[char] = True

    return tmp


def merge_dict(first, second):
    tmp = {}

    for key in second.keys():
        if first.get(key, False):
            tmp[key] = True

    return tmp


def solve(group):
    one = create_dict(group[0])
    two = merge_dict(one, create_dict(group[1]))
    three = merge_dict(two, create_dict(group[2]))

    key = list(three.keys())[0]
    return char_value(key)


def main():
    line = sys.stdin.readline()
    result = 0
    group = []

    while line:
        group.append(line)
        if len(group) == 3:
            result += solve(group)
            group = []
        line = sys.stdin.readline()

    print(result)


main()
