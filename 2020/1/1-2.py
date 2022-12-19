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
            for numb2 in numbs:
                if numb != numb2:
                    values[numb+numb2] = [numb, numb2]

        for numb in numbs:
            flag = values.get(2020 - numb, False)
            if flag:
                print("Found values", numb, flag, "With sum:", numb * flag[0] * flag[1])
                return;

    print("Not found :(")

main()
