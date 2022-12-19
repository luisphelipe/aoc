import os
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')
        

def main ():
    with open(input) as f:
        lines = f.read().splitlines()
        passports = [{}]
        index = 0

        required_docs = [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
            # "cid" # Not required
        ]

        valid_passports = 0

        for line in lines:
            if (not line):
                index += 1
                passports.append({})
                continue

            data = line.split(" ")

            for doc in data:
                [key, value] = doc.split(":")
                passports[index][key] = value

        for passport in passports:
            if all([doc in passport for doc in required_docs]):
                valid_passports += 1

        # print("-- Passports --")
        # pp(passports[0: 10])

        print(f"There are {len(passports)}, of wich {valid_passports} are valid!")

main()
