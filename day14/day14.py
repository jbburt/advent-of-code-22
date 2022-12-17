f = 'day14/data.txt'

with open(f, 'r') as of:
    content = of.read().strip()

# sand is pouring into the cave from point 500,0
# Sand keeps moving as long as it is able to do so, at each step trying to move
# down, then down-left, then down-right

rocks = set()
for line in content.split('\n'):
    prev = None
    for point in line.strip().split(' -> '):
        x, y = map(int, point.split(','))
        # print(x, y)

        if prev is None:
            prev = (x, y)
            rocks.add(prev)
            continue

        x0, y0 = prev

        if x == x0:
            diff = y - y0
            delta = 1 if diff > 0 else -1
            while y0 != y:
                y0 += delta
                rocks.add((x, y0))

        if y == y0:
            diff = x - x0
            delta = 1 if diff > 0 else -1
            while x0 != x:
                x0 += delta
                rocks.add((x0, y))

        # stuff
        prev = (x, y)
        # rocks.add(prev)

maxy = max(r[1] for r in rocks)
maxx = max(r[0] for r in rocks)
minx = min(r[0] for r in rocks)

objects = rocks.copy()
finished = False

while not finished:
    rest = False

    # sand falls
    sx, sy = (500, 0)

    # find final resting point
    while not rest:
        if sy > maxy or not (minx <= sx <= maxx):
            rest = finished = True
        if (sx, sy + 1) not in objects:
            sy += 1
        elif (sx - 1, sy + 1) not in objects:
            sx -= 1
            sy += 1
        elif (sx + 1, sy + 1) not in objects:
            sx += 1
            sy += 1
        else:
            rest = True
    if not finished:
        objects.add((sx, sy))
    if sx == 500 and sy == 0:
        finished = True

print(f'p1: {len(objects) - len(rocks)}')


floor = maxy + 2

objects = rocks.copy()
finished = False

while not finished:
    rest = False

    # sand falls
    sx, sy = (500, 0)

    # find final resting point
    while not rest:

        if (sy + 1) == floor:
            rest = True
        elif (sx, sy + 1) not in objects:
            sy += 1
        elif (sx - 1, sy + 1) not in objects:
            sx -= 1
            sy += 1
        elif (sx + 1, sy + 1) not in objects:
            sx += 1
            sy += 1
        else:
            rest = True

    if not finished:
        objects.add((sx, sy))

    if sx == 500 and sy == 0:
        finished = True

print(f'p2: {len(objects) - len(rocks)}')
