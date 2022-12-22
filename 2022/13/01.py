import sys
import pprint
import json

pp = pprint.PrettyPrinter(indent=4).pprint


def main():
    solution = solve()
    print("count is", solution)


def solve():
    result = []
    cont = True

    while cont:
        left = parse_list(sys.stdin.readline())
        right = parse_list(sys.stdin.readline())
        cont = sys.stdin.readline()

        res = compare_values(left, right)
        #  result.append((left, right))
        result.append(res)

    count = 0

    for i in range(len(result)):
        if result[i] == -1:
            count += i + 1

    return count


def parse_list(line):
    return json.loads(line)


def compare_values(left, right):
    for i in range(min(len(left), len(right))):
        lv = left[i]
        rv = right[i]

        if isinstance(lv, int) and isinstance(rv, int):
            if lv == rv:
                continue
            return -1 if lv < rv else 1

        if isinstance(lv, int):
            lv = [lv]
        if isinstance(rv, int):
            rv = [rv]

        res = compare_values(lv, rv)

        if res != 0:
            return res

    if len(left) == len(right):
        return 0

    return 1 if len(left) > len(right) else -1


main()
