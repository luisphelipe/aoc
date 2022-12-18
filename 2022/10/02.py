import sys
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint


class CPU:
    def __init__(self):
        self._op_queue = []
        self._screen = []

    def parse_op(self, op):
        self._op_queue.append(0)

        if op != "noop\n":
            incr = int(op.split(" ")[1])
            self._op_queue.append(incr)

    def process_ops(self):
        cycle, x = 1, 1
        screen = []

        while len(self._op_queue) > 0:
            x += self._op_queue.pop(0)

            if abs(cycle - x) <= 1:
                screen.append('o')
            else:
                screen.append(' ')

            cycle += 1

            if cycle > 40:
                cycle = 1

        self._screen = screen

    def print_screen(self):
        lines = []

        for i in range(6):
            print("".join(self._screen[i * 40:(i+1) * 40]))


def main():
    line = sys.stdin.readline()
    cpu = CPU()

    while line:
        cpu.parse_op(line)
        line = sys.stdin.readline()

    cpu.process_ops()
    cpu.print_screen()


main()
