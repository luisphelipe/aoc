import os

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')

def main ():
    with open(input) as f:
        lines = f.read().splitlines()
        correct = 0

        for line in lines:
            data = line.split(" ")
            [min, max] = [int(x) for x in data[0].split("-")]
            letter = data[1][0]
            word = data[2]
            count = 0

            for char in word:
                if char == letter: 
                    count += 1
        
            if count >= min and count <= max:
                correct += 1

        print(f'There are {correct} correct passwords')

main()
