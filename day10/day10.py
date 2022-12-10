f = 'day10/data.txt'

with open(f, 'r') as of:
    lines = of.read().strip().split('\n')

l = 0
cycle = 0
register = 1
strengths = {v: v for v in [20, 60, 100, 140, 180, 220]}

while l < len(lines):
    cycle += 1
    if cycle in strengths:
        strengths[cycle] *= register
    if (line := lines[l].strip()) == 'noop':
        pass
    else:
        increment = int(line.split()[-1])
        cycle += 1
        if cycle in strengths:
            strengths[cycle] *= register
        register += increment
    l += 1

print(f'part A: {sum(strengths.values())}')


crt = [[''] * 40 for _ in range(6)]

l = 0
cycle = 0
register = 1

while l < len(lines):
    cycle += 1
    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    print(row, col)
    crt[row][col] = '#' if abs(col - register) < 2 else '.'
    if (line := lines[l].strip()) == 'noop':
        pass
    else:
        increment = int(line.split()[-1])
        cycle += 1
        row = (cycle - 1) // 40
        col = (cycle - 1) % 40
        crt[row][col] = '#' if abs(col - register) < 2 else '.'
        register += increment
    l += 1

print('\n')
for line in crt:
    print(line)
# now squint
