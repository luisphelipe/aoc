import sys
from copy import deepcopy as copy


def main():

    result = 0
    stacks = build_stacks()
    print_stack(stacks)
    print("===>")

    final = process_operations(stacks)
    print_stack(final)
    print("===>")
    print(build_solution_string(final))


def build_stacks():
    line = sys.stdin.readline()
    stacks = [[] for i in range(9)]

    while line != "\n":
        if (line[0] == '1'):
            break

        values = build_line_values(line)

        for i in range(len(values)):
            stacks[i].append(values[i])

        line = sys.stdin.readline()

    stacks = [list(x)[0][::-1] for x in zip(stacks)]

    # remove white spaces
    for i in range(len(stacks)):
        stacks[i] = list(filter(lambda x: not x.isspace(), stacks[i]))

    return stacks


def build_line_values(string):
    values = []
    spaces = 0

    for char in string:
        if char == "\n":
            break
        if char == '[':
            values += [" "] * (spaces // 4)
        elif char == ']':
            spaces = -1
        elif char == " ":
            spaces += 1
        else:
            values.append(char)

    fill = [" "] * (9 - len(values))
    return fill + values


def print_stack(_stacks):
    stacks = copy(_stacks)
    length = 0

    for stack in stacks:
        length = max(len(stack), length)

    for i in range(length + 1, 0, -1):
        line = " "
        for stack in stacks:
            if len(stack) == i:
                line += f"[{stack.pop()}] "
            else:
                line += "    "
        line += ""
        print(line)


def process_operations(_stacks):
    line = sys.stdin.readline()
    stacks = copy(_stacks)

    while line == "\n":
        line = sys.stdin.readline()

    while line:
        stacks = process_move(stacks, line)
        line = sys.stdin.readline()

    return stacks


def process_move(stacks, line):
    n, a, b = interpret_query(line)
    stacks[b - 1] += stacks[a - 1][-n:]
    stacks[a - 1] = stacks[a - 1][0:-n]
    return stacks


def interpret_query(line):
    parts = line.split()
    return [int(parts[1]), int(parts[3]), int(parts[5])]


def build_solution_string(stacks):
    string = ""
    for stack in stacks:
        string += stack.pop() if len(stack) > 0 else ""
    return string


main()
