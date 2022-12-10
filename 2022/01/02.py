import sys


def main():
    total = []
    current = 0

    for line in sys.stdin:
        if line == "\n":
            total.append(current)
            current = 0
            continue

        current += int(line)

    print(sum(sorted(total)[-3:]))


main()
