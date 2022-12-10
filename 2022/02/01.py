import sys


def result(elf, you):
    if you == (elf + 1) % 3:
        return 6
    if you == elf:
        return 3
    return 0


def main():
    total = 0
    elf_options = 'ABC'
    you_options = 'XYZ'

    line = sys.stdin.readline()

    while line:
        elf, you = line.split()

        elfv = elf_options.find(elf)
        youv = you_options.find(you)

        total += result(elfv, youv) + youv + 1

        line = sys.stdin.readline()

    print(total)


main()
