import os
import math

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')

def main ():
    rules = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]

    with open(input) as f:
        lines = f.read().splitlines()
        height = len(lines)
        width = len(lines[0])
        min_trees = height
        min_rule = 0
        multiplication = 1

        for [w_delta, h_delta] in rules:
            print(w_delta, h_delta, end=" ")
            pos = w_delta
            trees_encountered = 0
            
            for h in range(h_delta, height, h_delta):
                if (pos >= width):
                    pos = pos % width
                
                if lines[h][pos] == "#":
                    trees_encountered += 1

                # new_line = list(lines[h])
                # new_line[pos] = "X" if new_line[pos] == "#" else "O"
                # print("".join(new_line))

                pos += w_delta

                
            if (trees_encountered < min_trees):
                min_trees = trees_encountered
                min_rule = rules.index([w_delta, h_delta])

            multiplication *= trees_encountered
            print(f"I encountered {trees_encountered} trees along the way!")

        
        print(f"The minimum amount of trees encountered was {min_trees} using the rule {rules[min_rule]}")
        print(f"The multiplicated value of each result was {multiplication}")


main()
