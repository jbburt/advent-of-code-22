f = 'day4/data.txt'

with open(f, 'r') as of:
    lines = of.read().rstrip('\n').split('\n')


def parse(l):
    return [tuple(sorted(map(int, elf.split('-')))) for elf in l.split(',')]


sections = [parse(l) for l in lines]
edges = [(min(l), max(r)) for l, r in [list(zip(*s)) for s in sections]]

caseA = caseB = 0
for extent, pairs in zip(edges, sections):
    if extent in pairs:
        caseA += 1
    else:
        (a, b), (c, d) = pairs
        if c <= a <= d or c <= b <= d:
            caseB += 1

print(f'part A: {caseA}')
print(f'part B: {caseA + caseB}')
