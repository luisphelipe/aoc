import sys
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint


class CPU:
    def __init__(self):
        self._op_queue = []

    def parse_op(self, op):
        self._op_queue.append(0)

        if op != "noop\n":
            incr = int(op.split(" ")[1])
            self._op_queue.append(incr)

    def process_ops(self):
        cycle, x, result = 1, 1, 0

        while len(self._op_queue) > 0:
            val = self._op_queue.pop(0)
            x += val

            cycle += 1

            if (cycle - 20) % 40 == 0:
                result += x * cycle

        return result


def main():
    line = sys.stdin.readline()
    cpu = CPU()

    while line:
        cpu.parse_op(line)
        line = sys.stdin.readline()

    result = cpu.process_ops()
    print(result)


main()
