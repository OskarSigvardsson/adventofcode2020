def van_eck(start):
    yield from start[:-1]

    last = { v:i for i,v in enumerate(start[:-1]) }
    i = len(start) - 1
    n = start[-1]

    while True:
        yield n
        nxt = -1

        if n in last:
            nxt = i - last[n]
        else:
            nxt = 0
        
        last[n] = i
        n = nxt
        i += 1

def solve(start, index):
    return [n for _,n in zip(range(index), van_eck(start))][index-1]

print("Part 1:", solve([9,3,1,0,8,4], 2020))
print("Part 2:", solve([9,3,1,0,8,4], 30000000))

