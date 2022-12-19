import os
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint

local = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(local, 'input')
        
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

def between(val, min, max):
    return val >= min and val <= max

def has_all_required_fields(passport):
    return all([doc in passport for doc in required_docs])

def valid_byr(byr):
    num = int(byr)
    return (len(byr) == 4 and between(num, 1920, 2002))

def valid_iyr(iyr):
    num = int(iyr)
    return (len(iyr) == 4 and between(num, 2010, 2020))

def valid_eyr(eyr):
    num = int(eyr)
    return (len(eyr) == 4 and between(num, 2020, 2030))

def valid_hgt(hgt):
    num = int(hgt[0:-2])
    return (
        between(num, 150, 193) if hgt[-2:] == "cm" else between(num, 59, 76)
    )

def valid_hcl(hcl):
    hexlist = list("0123456789abcdef")
    return (
        hcl[0] == "#" and all(char in hexlist for char in hcl[1:]) and len(hcl[1:]) == 6
    )

def valid_ecl(ecl):
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid

def valid_pid(pid):
    valid = list("0123456789")
    return (len(pid) == 9 and all(char in valid for char in pid))


def valid_passport(passport): 
    return (
        has_all_required_fields(passport) and
        valid_byr(passport['byr']) and
        valid_iyr(passport['iyr']) and
        valid_eyr(passport['eyr']) and
        valid_hgt(passport['hgt']) and
        valid_hcl(passport['hcl']) and
        valid_ecl(passport['ecl']) and
        valid_pid(passport['pid'])
    )

    
def main ():
    with open(input) as f:
        lines = f.read().splitlines()
        passports = [{}]
        index = 0

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
            if valid_passport(passport):
                valid_passports += 1

        # print("-- Passports --")
        # pp(passports[0: 10])

        print(f"There are {len(passports)}, of wich {valid_passports} are valid!")

main()
