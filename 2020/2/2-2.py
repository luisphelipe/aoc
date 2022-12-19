import os

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')

def main ():
    with open(input) as f:
        lines = f.read().splitlines()
        correct = 0

        for line in lines:
            data = line.split(" ")
            [first, second] = [int(x) - 1 for x in data[0].split("-")]
            letter = data[1][0]
            word = data[2]

            valid = word[first] != word[second] and \
                (word[first] == letter or word[second] == letter)

            if valid:
                correct += 1
        
        print(f'There are {correct} correct passwords')

main()
