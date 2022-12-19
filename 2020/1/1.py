import os

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')

def main ():
    sum = 0;
    values = {}

    with open(input) as f:
        lines = f.read().splitlines()
        numbs = [int(x) for x in lines]
        numbs.sort()

        for numb in numbs:
            values[numb] = True;

        for numb in numbs:
            flag = values.get(2020 - numb, False)
            if flag:
                print("Found value", numb, "With sum:", numb * (2020-numb))
                return;

    print("Not found :(")

main()
