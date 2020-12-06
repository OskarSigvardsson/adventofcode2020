import re

def parse(text):
    entries = [" ".join(f.split("\n")).strip() for f in text.split("\n\n")]

    passports = []
    for entry in entries:
        current = {}

        for field in entry.split(" "):
            key, val = field.split(":")
            current[key] = val

        passports.append(current)

    return passports


def valid1(passport):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    return all(field in passport for field in required)


def valid_height(entry):
    if m := re.match(r"(\d+)cm$", entry):
        return 150 <= int(m.group(1)) <= 193

    elif m := re.match(r"(\d+)in$", entry):
        return 59 <= int(m.group(1)) <= 76

    else:
        return False


def valid2(passport):
    check = {
        "byr": lambda v: 1920 <= int(v) <= 2002,
        "iyr": lambda v: 2010 <= int(v) <= 2020,
        "eyr": lambda v: 2020 <= int(v) <= 2030,
        "hgt": valid_height,
        "hcl": lambda v: re.match(r"#[0-9a-f]{6}$", v),
        "ecl": lambda v: re.match(r"(amb|blu|brn|gry|grn|hzl|oth)$", v),
        "pid": lambda v: re.match(r"[0-9]{9}$", v),
        "cid": lambda v: True,
    }

    return valid1(passport) and all(
        check[key](value) for key,value in passport.items()
    )


with open("input.txt", "r") as f:
    passports = parse(f.read())

    print(len([passport for passport in passports if valid1(passport)]))
    print(len([passport for passport in passports if valid2(passport)]))
