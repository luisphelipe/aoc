import sys
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint


class CheckLogic:
    def __init__(self, op, right):
        self.op = op
        self.right = right

    def apply(self, item):
        op = self.op
        left = item
        right = item if self.right == "ITEM" else self.right

        if op == "+":
            return left + right
        if op == "-":
            return left - right
        if op == "*":
            return left * right
        if op == "/":
            return left / right


class ThrowLogic:
    def __init__(self, div, op1, op2):
        self.div = div
        self.op1 = op1
        self.op2 = op2

    def apply(self, item):
        if item % self.div == 0:
            return self.op1
        return self.op2


class Monke:
    def __init__(self, items, check_logic, throw_logic):
        self._items = items
        self.business = 0
        self._check_logic = check_logic
        self._throw_logic = throw_logic

    def check(self):
        items = []
        for item in self._items:
            new_item = self._check_logic.apply(item)
            new_item = new_item // 3
            items.append(new_item)
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


class MonkePlay:
    def __init__(self):
        self._monkes = [
            Monke(
                [71, 86],
                CheckLogic("*", 13),
                ThrowLogic(19, 6, 7)
            ),
            Monke(
                [66, 50, 90, 53, 88, 85],
                CheckLogic("+", 3),
                ThrowLogic(2, 5, 4)
            ),
            Monke(
                [97, 54, 89, 62, 84, 80, 63],
                CheckLogic("+", 6),
                ThrowLogic(13, 4, 1)
            ),
            Monke(
                [82, 97, 56, 92],
                CheckLogic("+", 2),
                ThrowLogic(5, 6, 0)
            ),
            Monke(
                [50, 99, 67, 61, 86],
                CheckLogic("*", "ITEM"),
                ThrowLogic(7, 5, 3)
            ),
            Monke(
                [61, 66, 72, 55, 64, 53, 72, 63],
                CheckLogic("+", 4),
                ThrowLogic(11, 3, 0)
            ),
            Monke(
                [59, 79, 63],
                CheckLogic("*", 7),
                ThrowLogic(17, 2, 7)
            ),
            Monke(
                [55],
                CheckLogic("+", 7),
                ThrowLogic(3, 2, 1)
            ),
        ]

    def round(self, round):
        for monke in self._monkes:
            monke.count()
            monke.check()
            monke.throw(self._monkes)

        self.print_monke_business(round)

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


def main():
    mp = MonkePlay()

    for i in range(20):
        mp.round(i + 1)


main()
