from itertools import combinations

numbers = []

with open("input.txt", "r") as f:
    numbers = [int(line) for line in f]


def part1(numbers):
    for i in range(25, len(numbers)):
        target = numbers[i]

        # combinations(iterable, 2) is a generator that returns all
        # 2-combinations from a sequence. So list(combinations([1,2,3], 2)) is
        # equal to [(1,2), (1,3), (2,3)].
        #
        # You could do this with nested loops, but what fun is that? 
        if not any(True for a,b in combinations(numbers[i-25:i], 2) if a+b == target):
            return target
            
def part2(numbers):
    # I'm almost certain there's a MUCH faster algorithm for this, where you
    # have this sliding window you move over the list, but i just did this dumb
    # one and it works fine (finishes in roughly a second, which isn't great,
    # but isn't horrifying), so I'm sticking with it.
    target = part1(numbers)

    for i in range(len(numbers) - 1):
        for j in range(i + 2, len(numbers)):
            sublist = numbers[i:j]

            if target == sum(sublist):
                return min(sublist) + max(sublist)
        
            if target < sum(sublist):
                # Increasing j is only going to increase the sum, and the sum is
                # already past the target, so might as well break the inner
                # loop. This is a significant performance improvement. 
                break

print(part1(numbers))
print(part2(numbers))
