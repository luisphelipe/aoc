import os

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')

def main ():
    with open(input) as f:
        lines = f.read().splitlines()
        height = len(lines)
        width = len(lines[0])
        pos = 3
        trees_encountered = 0
        
        for h in range(1, height):
            if (pos >= width):
                pos = pos % width
            
            if lines[h][pos] == "#":
                trees_encountered += 1

            pos += 3


        print(f"I encountered {trees_encountered} trees along the way!")
        

main()
