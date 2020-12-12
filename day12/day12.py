import re

instructions = []

with open("input.txt", "r") as f:
    for line in f:
        c,v = re.match("(.)(.+)", line).groups()

        v = int(v)

        if c == "R":
            c = "L"
            v = 360 - v

        if c == "L":
            v = int(v/90)

        instructions.append((c, v))

def part1(instructions):
    dirs = {
        "E":  1 +  0j,
        "N":  0 +  1j,
        "W": -1 +  0j,
        "S":  0 + -1j,
    }

    pos = 0+0j
    heading = 1+0j

    for c,v in instructions:
        if c == "F":
            pos += v * heading

        elif c == "L":
            heading *= 1j ** v

        else:
            pos += v * dirs[c]

    return abs(pos.real) + abs(pos.imag)

def part2(instructions):
    dirs = {
        "E":  1 +  0j,
        "N":  0 +  1j,
        "W": -1 +  0j,
        "S":  0 + -1j,
    }

    pos = 0+0j
    heading = 10+1j

    for c,v in instructions:
        if c == "F":
            pos += v * heading

        elif c == "L":
            heading *= 1j ** v

        else:
            heading += v * dirs[c]

    return abs(pos.real) + abs(pos.imag)

print(part1(instructions))
print(part2(instructions))
