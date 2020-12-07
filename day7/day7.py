import re

lines = []

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

#--------+
# Part 1 |
#--------+
def can_contain(rules, outer, inner):
    for bag in rules[outer]:
        if bag == inner:
            return True

        if can_contain(rules, bag, inner):
            return True

    return False

def part1(lines):
    rules = {}

    for line in lines:
        rule = re.findall(r"(\w+ \w+) bags?", line)

        rules[rule[0]] = rule[1:] if rule[1] != "no other" else []

    return [bag for bag in rules if can_contain(rules, bag, "shiny gold")]


print(len(part1(lines)))


#--------+
# Part 2 |
#--------+
def count_bags(rules, outer, indent = 0):
    total = 1

    for count, inner in rules[outer]:
        total += count * count_bags(rules, inner, indent+2)

    return total

def part2(lines):
    rules = {}

    for line in lines:
        outer = re.match(r"^(\w+ \w+) bags", line)
        inner = re.findall(r"(\d+) (\w+ \w+)", line)

        rules[outer.group(1)] = [(int(count), bag) for count,bag in inner]

    return count_bags(rules, "shiny gold") - 1


print(part2(lines))
