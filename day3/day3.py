lines = []

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def impacts(lines, dx, dy):
    width = len(lines[0])
    x, y = 0, 0
    count = 0

    while y < len(lines):
        if lines[y][x] == '#':
            count += 1

        x = (x + dx) % width
        y += dy

    return count


print(impacts(lines, 3, 1))
print(impacts(lines, 1, 1)
    * impacts(lines, 3, 1)
    * impacts(lines, 5, 1)
    * impacts(lines, 7, 1)
    * impacts(lines, 1, 2))
