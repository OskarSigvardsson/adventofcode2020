import re

instructions = []

with open("input.txt", "r") as f:
    for line in f:
        if m := re.match("mask = (.+)", line):
            instructions.append(("mask", (m.group(1),)))
        elif m := re.match(r"mem\[(.+)\] = (.+)", line):
            loc, val = m.groups()
            instructions.append(("set", (int(loc), int(val))))
        else:
            print("error: ", line)
            exit(1)


def part1(instructions):
    mask_val = 0
    mask = 0

    mem = {}
    
    for op,args in instructions:
        if op == "mask":
            mask_val = int(args[0].replace("X", "0"), 2)
            mask = int(args[0].replace("X", "1"), 2)
        else:
            loc,val = args
            mem[loc] = (val & mask) | mask_val

    return sum(mem.values())


def part2(instructions):
    ops = []
    
    for op,args in instructions:
        if op == "mask":
            mask_val = int(args[0].replace("X", "0"), 2)
            bits = [i for i,c in enumerate(reversed(args[0])) if c == "X"]
            ops.append(("mask", args[0], bits))
        else:
            loc,val = args
            ops.append(("set", loc, val))
        

    mask_and = 0
    mask_or = 0
    mask_bits = []
    mem = {}
    
    for op,a,b in ops:
        if op == "mask":
            mask_and = int(a.replace("0","1").replace("X","0"),2)
            mask_or  = int(a.replace("X","0"), 2)
            mask_bits = b
        else:
            val = b

            for ctr in range(2**len(mask_bits)):
                loc = (a & mask_and) | mask_or

                for j,bit in enumerate(mask_bits):
                    if ((ctr >> j) & 1) == 1:
                        loc |= (1 << bit)
                    else:
                        loc &= -1 ^ (1 << bit)

                mem[loc] = val



    return sum(mem.values())

print(part1(instructions))
print(part2(instructions))

