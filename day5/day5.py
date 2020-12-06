import re

nums = []

with open("input.txt", "r") as f:
    # The seat ID is just the code in binary, and int(x, 2) converts a string of
    # 1's and 0's to it's equivalent binary number
    nums = [int(line.strip()
            .replace("B", "1")
            .replace("R", "1")
            .replace("F", "0")
            .replace("L", "0"), 2)
        for line in f]

def part1(nums):
    return max(nums)

def part2(nums):
    nums.sort()

    # Pair up elements with their successor, find the pair(s) that are 2 apart
    return [a+1 for a,b in zip(nums, nums[1:]) if b != a+1]

print(part1(nums))
print(part2(nums))

