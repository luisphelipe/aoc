import sys
import pprint
import json
from functools import cmp_to_key

pp = pprint.PrettyPrinter(indent=4).pprint


def main():
    solution = solve()
    print("result is", solution)


def solve():
    cont = True
    a, b = [[2]], [[6]]
    values = [a, b]

    while cont:
        left = parse_list(sys.stdin.readline())
        right = parse_list(sys.stdin.readline())
        cont = sys.stdin.readline()
        values.append(left)
        values.append(right)

    values.sort(key=cmp_to_key(compare_values))
    #  pp(values)
    inda = values.index(a) + 1
    indb = values.index(b) + 1
    result = inda * indb
    return result


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
