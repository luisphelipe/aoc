import os

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')

def main ():
    with open(input) as f:
        lines = f.read().splitlines()
        plane = [None] * 2 ** 10
        # print(plane)

        for line in lines:
            data = line.split(" ")[0]

            seat = int(\
                data[0:7].replace('B', '1').replace('F', '0') + \
                data[7:].replace('R', '1').replace('L', '0'), 2)

            plane[seat] = True 
        
        # print(plane)

        for seat in range(2 ** 10 - 1, 0, -1):
            if plane[seat]:
                print(f"Last used seat id is {seat}")
                return

        # print("implementation missing")

main()
