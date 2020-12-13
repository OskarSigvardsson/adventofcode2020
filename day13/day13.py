earliest = 0
buses = []

with open("input.txt", "r") as f:
    earliest = int(f.readline().strip())
    buses = f.readline().split(",")


def part1(earliest, buses):
    buses = [int(bus) for bus in buses if bus != "x"]

    dep, bus = min((bus - (earliest % bus), bus) for bus in buses)

    return dep * bus

def part2(buses):
    # This relies on something called the Chinese Remainder Theorem. I think it
    # only works if the buses are all pairwise coprime, but apparently they are,
    # because it gave the right answer.
    congruences = [(-i % int(bus), int(bus)) for i,bus in enumerate(buses) if bus != 'x']

    x,m = congruences[0]

    for a,n in congruences[1:]:
        while x % n != a:
            x += m

        m *= n
        
    return x
    
print(part1(earliest, buses))
print(part2(buses))
