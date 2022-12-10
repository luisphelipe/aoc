import sys


def calculate_hand(elf, you):
    if you == 2:
        return (elf + 1) % 3
    if you == 1:
        return elf
    return elf - 1 if elf - 1 >= 0 else 2


def calculate_match(line):
    elf_options = 'ABC'
    you_options = 'XYZ'

    elf, you = line.split()
    elf_value = elf_options.find(elf)
    your_value = you_options.find(you)

    result_value = calculate_hand(elf_value, your_value)
    hand_value = result_value + 1 + your_value * 3

    return hand_value


def main():
    total = 0

    match = sys.stdin.readline()

    while match:
        total += calculate_match(match)
        match = sys.stdin.readline()

    print(total)


main()
