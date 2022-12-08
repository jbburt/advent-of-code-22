f = 'day8/data.txt'

with open(f, 'r') as of:
    rows = of.read().strip().split('\n')

nrow = len(rows[0])
ncol = len(rows)

nvisible = 0
visible = set()

# row-wise
for i in range(nrow):
    tallest = -1
    for j, height in enumerate(map(int, rows[i])):
        if height > tallest:
            tallest = height
            if (point := (i, j)) not in visible:
                nvisible += 1
                visible.add(point)

# rev row-wise
for i in range(nrow):
    tallest = -1
    for k, height in enumerate(map(int, reversed(rows[i]))):
        if height > tallest:
            tallest = height
            if (point := (i, ncol - 1 - k)) not in visible:
                nvisible += 1
                visible.add(point)

# col-wise
for j in range(ncol):
    tallest = -1
    for i, height in enumerate(map(int, [r[j] for r in rows])):
        if height > tallest:
            tallest = height
            if (point := (i, j)) not in visible:
                nvisible += 1
                visible.add(point)

# rev row-wise
for j in range(ncol):
    tallest = -1
    for k, height in enumerate(map(int, reversed([r[j] for r in rows]))):
        if height > tallest:
            tallest = height
            if (point := (nrow - 1 - k, j)) not in visible:
                nvisible += 1
                visible.add(point)

print(f'part A: {nvisible}')


optimal = 0

# ignore edges as scenic score will be zero
for row in range(1, nrow - 1):
    for col in range(1, ncol - 1):

        height = int(rows[row][col])
        score = 1

        # looking left/right
        for delta in [-1, 1]:
            j = col + delta
            n = 1
            while (0 < j < ncol - 1) and (int(rows[row][j]) < height):
                n += 1
                j += delta
            score *= n

        # looking down/up
        for delta in [-1, 1]:
            i = row + delta
            n = 1
            while (0 < i < nrow - 1) and (int(rows[i][col]) < height):
                n += 1
                i += delta
            score *= n

        if score > optimal:
            optimal = score

print(f'part B: {optimal}')
