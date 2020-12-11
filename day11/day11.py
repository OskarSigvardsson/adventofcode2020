from copy import deepcopy

lines = []

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

def part1(seats):
    adj = [(a,b)
           for a in range(-1, 2)
           for b in range(-1, 2)
           if not (a == 0 and b == 0)]

    width = len(seats[0])

    # Add a "ring" of dots around the seats. This makes the later code simpler,
    # no need to check bounds
    seats = ["." * width] + seats + ["." * width]
    seats = [list("." + row + ".") for row in seats]

    while True:
        new_seats = deepcopy(seats)

        changed = False
        for y in range(len(seats)):
            for x in range(len(seats[0])):
                if seats[y][x] == ".":
                    continue
                
                count = sum(1 for dx,dy in adj if seats[y+dy][x+dx] == "#")

                if seats[y][x] == "L" and count == 0:
                    new_seats[y][x] = "#"
                    changed = True
                elif seats[y][x] == "#" and count >= 4:
                    new_seats[y][x] = "L"
                    changed = True

        if not changed:
            return sum(sum(1 for seat in row if seat == "#") for row in new_seats)

        seats = new_seats


def part2(seats):
    adj = [(a,b)
           for a in range(-1, 2)
           for b in range(-1, 2)
           if not (a == 0 and b == 0)]

    width = len(seats[0])

    # Again, to avoid checking bounds
    seats = ["x" * width] + seats + ["x" * width]
    seats = [list("x" + row + "x") for row in seats]

    while True:
        new_seats = deepcopy(seats)

        changed = False
        for y in range(1, len(seats) - 1):
            for x in range(1, len(seats[0]) - 1):
                if seats[y][x] == ".":
                    continue
                
                count = 0

                for dx,dy in adj:
                    vx, vy = x+dx, y+dy
                    while seats[vy][vx] == ".":
                        vx, vy = vx+dx, vy+dy
                        
                    if seats[vy][vx] == "#":
                        count += 1
                    

                if seats[y][x] == "L" and count == 0:
                    new_seats[y][x] = "#"
                    changed = True
                elif seats[y][x] == "#" and count >= 5:
                    new_seats[y][x] = "L"
                    changed = True

        if not changed:
            return sum(sum(1 for seat in row if seat == "#") for row in new_seats)

        seats = new_seats

print(part1(lines))
print(part2(lines))
