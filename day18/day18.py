import itertools
from collections import defaultdict

with open('day18/data.txt', 'r') as of:
    lines = of.read().strip().split('\n')

cubes = set(list(map(lambda n: tuple(map(int, n.strip().split(','))), lines)))

deltas = [
    (0.5, 0, 0), (-0.5, 0, 0),
    (0, 0.5, 0), (0, -0.5, 0),
    (0, 0, 0.5), (0, 0, -0.5)
]

edges = defaultdict(int)
for x, y, z in cubes:
    for dx, dy, dz in deltas:
        edges[(x + dx, y + dy, z + dz)] += 1
p1 = sum(v == 1 for k, v in edges.items())
print(f'p1: {p1}')

# notice that the cubes fill a 20^3 grid in the +,+,+ octant
side = 20

# empty space within the grid
space = set(list(itertools.product(*(range(side) for _ in range(3)))))
space.difference_update(cubes)

# find contiguous blocks of vacant space
blocks = list()
while space:
    region = {space.pop()}
    queue = list(region)
    while queue:
        pos = queue.pop()
        for dim in range(3):
            for step in (1, -1):
                other = list(pos)
                other[dim] += step
                other = tuple(other)
                if other in space:
                    region.add(other)
                    queue.append(other)
                    space.remove(other)
    blocks.append(region)

# solve p2 by subtracting surface area of interior blocks from p1 solution
p2 = p1
for i, block in enumerate(blocks):
    # if a contiguous block is interior, it will not extend to the boundary
    flat = [x for point in block for x in point]
    if min(flat) == 0 or max(flat) == side - 1:  # exterior
        continue
    # find surface area of interior block and subtract
    sa = 0
    for point in block:
        for dim in range(3):
            for step in (1, -1):
                tmp = list(point)
                tmp[dim] += step
                if tuple(tmp) in cubes:
                    sa += 1
    p2 -= sa
print(f'p2: {p2}')
