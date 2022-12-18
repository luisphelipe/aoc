import sys
import pprint
from time import time

#  pp = pprint.PrettyPrinter(indent=4).pprint
pp = pprint.PrettyPrinter().pprint


def main():
    NUM_OF_MONKEYS = 8
    NUM_OF_ROUNDS = 10_000
    #  NUM_OF_MONKEYS = 4
    #  NUM_OF_ROUNDS = 20

    mp = MonkePlay(NUM_OF_MONKEYS)

    for i in range(NUM_OF_ROUNDS):
        mp.round(i + 1)


class MonkePlay:
    def __init__(self, number_of_monkeys):
        monkeBuilder = MonkeBuilder()
        monkes = []
        multiple = 1

        for _ in range(number_of_monkeys):
            monke = monkeBuilder.buildMonke()
            multiple *= monke.getDiv()
            monkes.append(monke)

        self._monkes = monkes
        self._multiple = multiple

    def round(self, round):
        times = []
        st = time()

        for monke in self._monkes:
            monke.count()
            times.append(f"to count: {time() - st:.6}")

            monke.check(self._multiple)
            times.append(f"to check: {time() - st:.6}")

            monke.throw(self._monkes)
            times.append(f"to throw: {time() - st:.6}")

        if round % 1000 == 0 or round == 1 or round == 20:
            #  pp(times)
            self.print_monke_business(round)
            #  print("")

    def print_monke_business(self, round):
        print(f"round {round:02}", end=" => ")
        b = []

        for monke in self._monkes:
            b.append(monke.business)

        print(b, end=" => ")
        b = sorted(b)[-2:]
        bt = b[0] * b[1]

        print(b, end=" => ")
        print("total =", bt)


class MonkeBuilder:
    def buildMonke(self):
        name = self.getName()
        items = self.getStartingItems()
        checkLogic = self.getCheckLogic()
        throwLogic = self.getThrowLogic()
        sys.stdin.readline()
        #  print("building monke", name)
        #  print("items", items)
        #  print("checkLogic", checkLogic)
        #  print("throwLogic", throwLogic)
        #  print()
        monke = Monke(name, items, checkLogic, throwLogic)
        return monke

    def getName(self):
        line = sys.stdin.readline()[:-1]
        name = line.replace(" ", "")
        return name

    def getStartingItems(self):
        line = sys.stdin.readline()[:-1]
        items = line.split(": ")[1].split(", ")
        items = [int(x) for x in items]
        return items

    def getCheckLogic(self):
        line = sys.stdin.readline()[:-1]
        line = line.split("= old ")[1]
        op, right = line.split(" ")
        if right == "old":
            right = "ITEM"
        else:
            right = int(right)

        return CheckLogic(op, right)

    def getThrowLogic(self):
        line = sys.stdin.readline()[:-1]
        div = int(line.split("by ")[1])

        line = sys.stdin.readline()[:-1]
        op1 = int(line.split("monkey ")[1])

        line = sys.stdin.readline()[:-1]
        op2 = int(line.split("monkey ")[1])

        return ThrowLogic(div, op1, op2)


class Monke:
    def __init__(self, name, items, check_logic, throw_logic):
        self._name = name
        self._items = items
        self.business = 0
        self._check_logic = check_logic
        self._throw_logic = throw_logic

    def check(self, multiple):
        items = []
        for item in self._items:
            new_item = self._check_logic.apply(item)
            new_item = new_item % multiple
            items.append(new_item)
        #  print(self._name, div, self._items, '=>', items)
        self._items = items

    def throw(self, monkes):
        while (self._items):
            item = self._items.pop(0)
            monke = self._throw_logic.apply(item)
            monkes[monke].catch(item)

    def count(self):
        self.business += len(self._items)

    def catch(self, item):
        self._items.append(item)

    def getDiv(self):
        return self._throw_logic.getDiv()


class CheckLogic:
    def __init__(self, op, right):
        self.op = op
        self.right = right

    def apply(self, item):
        op = self.op
        left = item
        right = item if self.right == "ITEM" else self.right

        new_item = item

        if op == "+":
            return left + right
        if op == "-":
            return left - right
        if op == "*":
            return left * right
        if op == "/":
            return left / right

    def __repr__(self):
        return f"ITEM {self.op} {self.right}"


class ThrowLogic:
    def __init__(self, div, op1, op2):
        self.div = div
        self.op1 = op1
        self.op2 = op2

    def apply(self, item):
        if item % self.div == 0:
            return self.op1
        return self.op2

    def getDiv(self):
        return self.div

    def __repr__(self):
        return f"{self.div} ? {self.op1} : {self.op2}"


main()
