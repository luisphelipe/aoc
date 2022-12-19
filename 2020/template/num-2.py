import os

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')

def main ():
    with open(input) as f:
        lines = f.read().splitlines()

        for line in lines:
            data = line.split(" ")
        

        print("implementation missing")

main()
