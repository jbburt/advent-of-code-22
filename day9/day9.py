f = 'day9/data.txt'

with open(f, 'r') as of:
    lines = of.read().strip().split('\n')
motions = list(map(lambda c: (c[0], int(c[1])), [l.split() for l in lines]))


def delta(hx, hy, tx, ty):
    return hx - tx, hy - ty


def l1(dx_, dy_):
    # l1/manhattan distance
    return abs(dx_) + abs(dy_)


def chebyshev(dx_, dy_):
    # chebyshev distance
    return max(abs(dx_), abs(dy_))


# direction -> (dx, dy)
dirmap = dict(
    R=(1, 0),
    L=(-1, 0),
    U=(0, 1),
    D=(0, -1)
)

# (l1, chebyshev) pairs which require no action (due to adjacency)
skip = {(0, 0), (1, 1), (2, 1)}


def update(k):
    x0, y0 = knots[k - 1]
    xk, yk = knots[k]
    dx, dy = delta(x0, y0, xk, yk)
    if (dX := (dx, dy)) in cache:
        dxk, dyk = cache[dX]
    else:
        state = (l1(*dX), chebyshev(*dX))
        l1d, cd = state
        if state in skip:
            raise StopIteration

        dxk = 0 if not dx else int(dx / abs(dx))
        dyk = 0 if not dy else int(dy / abs(dy))
        assert dxk < 2 and dyk < 2

        if l1d == cd:  # rectilinearly separated
            if not dx:
                dxk = 0
            else:
                dyk = 0
        else:  # diagonally separated
            pass
        cache[dX] = (dxk, dyk)
    knots[k] = (xk + dxk, yk + dyk)


cache = dict()
knots = list()


def simulate(n_knots):
    global knots

    # visited grid locations
    visited = {(0, 0)}

    knots = [(0, 0) for _ in range(n_knots + 1)]

    for d, n in motions:
        dxh, dyh = dirmap[d]

        # foreach step
        for _ in range(n):

            # update head pos
            xh, yh = knots[0]
            xh += dxh
            yh += dyh
            knots[0] = (xh, yh)

            # move each subsequent knot sequentially
            for i in range(1, n_knots + 1):
                try:
                    update(i)
                except StopIteration:
                    break

            if (tpos := knots[-1]) not in visited:
                visited.add(tpos)

    return len(visited)


print(f'part A: {simulate(1)}')
print(f'part B: {simulate(9)}')
