
instructions = []

with open("input.txt", "r") as f:
    instructions = [[op, int(arg)] for op,arg in (line.split(" ") for line in f)]
    
# Returns a (bool, int) tuple, the first bool indicating whether or not the
# program halted normally, the second int being the accumulator.
#
# Fun fact: this function is impossible to write for "real" programming
# languages: this is the "halting problem", which Alan Turing proved impossible
# to solve for general computational models. The paper where he proved this ("On
# Computable Numbers") is literally the foundation for the entire field of
# Computer Science.
def halts(instructions):
    # "ip" stands for "instruction pointer", which is the traditional name for
    # this variable in virtual machines.
    ip = 0
    acc = 0
    visited = set()

    # Functions that return the new values for ip and acc, depending on the
    # opcode and argument
    operations = {
        "nop": lambda arg: (ip + 1, acc),
        "acc": lambda arg: (ip + 1, acc + arg),
        "jmp": lambda arg: (ip + arg, acc),
    }


    while ip < len(instructions) and ip not in visited:
        visited.add(ip)
        op, arg = instructions[ip]

        ip, acc = operations[op](arg)

    
    if ip == len(instructions):
        return True, acc
    else:
        return False, acc



def part1(instructions):
    return halts(instructions)[1] 


def part2(instructions):
    for i in range(len(instructions)):
        op, arg = instructions[i]

        if op == "acc":
            continue

        # Toggles "nop" to "jmp" or "jmp" to "nop"
        instructions[i][0] = "nop" if op == "jmp" else "jmp"

        did_halt, acc = halts(instructions)

        if did_halt:
            return acc

        # Restore instruction
        instructions[i][0] = op

    return -1

print(part1(instructions))
print(part2(instructions))
