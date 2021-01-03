from itertools import product
from functools import reduce

living = set()

with open("input.txt") as f:
    # lines = [line.strip for line in f.readlines())]

    for y,line in enumerate(f):
        for x,c in enumerate(line.strip()):
            if c == '#':
                living.add((x,y))

# wrote this for Part 1, but am not using it any more. the one_step() function
# below generalizes it to arbitrary dimensions, but I figured I'd leave it in.
# The other function is identical except that it's generalized. 
def one_step_3d(living):
    deltas = [(dx,dy,dz)
                for dx in [-1,0,1]
                for dy in [-1,0,1]
                for dz in [-1,0,1]]

    def count(x,y,z):
        return sum(1 for dx,dy,dz in deltas
                   if (dx,dy,dz) != (0,0,0) and (x+dx,y+dy,z+dz) in living)
                 
    # set of cells that might contain new births
    relevant = set((x+dx,y+dy,z+dz)
                   for x,y,z in living
                   for dx,dy,dz in deltas)

    # dead cells that have been reborn 
    reborn = set(cell for cell in relevant if cell not in living and count(*cell) == 3)

    # alive cells that are staying alive
    staying_alive = set(cell for cell in living if 2 <= count(*cell) <= 3)

    return reborn.union(staying_alive)


def one_step(living, dims):
    deltas = list(product([-1,0,1], repeat=dims))
    
    # Adds two vectors of dims dimensions together
    def add(v1, v2):
        return tuple(v1[i]+v2[i] for i in range(dims))
    
    # Counts all alive neighbors
    def count(coord):
        return sum(1 for n in deltas if n != (0,)*dims and add(coord,n) in living)
                 
    relevant = set(add(coord, neighbor)
                   for coord in living
                   for neighbor in deltas)

    # dead cells that have been reborn 
    reborn = set(cell for cell in relevant if cell not in living and count(cell) == 3)

    # alive cells that are staying alive
    staying_alive = set(cell for cell in living if 2 <= count(cell) <= 3)

    return reborn.union(staying_alive)


def simulate(living, dims, steps):
    living = set((x,y) + (0,) * (dims-2) for x,y in living)

    for _ in range(steps):
        living = one_step(living, dims)

    return living


# debug function i wrote while developing. Normally i delete these, but whatevs
def debug(living):
    minx, miny, minz = 0,0,0
    maxx, maxy, maxz = 0,0,0

    for x,y,z in living:
        minx = min(minx, x)
        miny = min(miny, y)
        minz = min(minz, z)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        maxz = max(maxz, z)
    
    print((minx,maxx))
    print((miny,maxy))
    print((minz,maxz))
    print()
    
    for z in range(minz, maxz+1):
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                print('#' if (x,y,z) in living else '.', end='')

            print()

        print()

#debug(simulate(living, 3, 2))
print(len(simulate(living, 3, 6)))
print(len(simulate(living, 4, 6)))
