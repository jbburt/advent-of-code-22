import re
from collections import deque

f = 'day5/data.txt'

pat1 = r'\[([A-Z])\]'
pat2 = r'move ([\d]+) from ([\d]) to ([\d])'

with open(f, 'r') as fp:
    # determine number of crate stacks
    while (line := fp.readline().strip())[0] != '1':
        continue
    num_stacks = int(line.split()[-1])

    # store byte offset
    _ = fp.readline()
    offs = fp.tell()
    fp.seek(0)

    # build crate stacks
    stacksA = [deque(list()) for _ in range(num_stacks)]
    while line := fp.readline().rstrip('\n'):
        for i in range(0, len(line), 4):
            if line[i + 1].isalpha():
                stacksA[i // 4].append(line[i + 1])
    stacksB = [s.copy() for s in stacksA]

    # parse moves
    fp.seek(offs)
    while line := fp.readline().strip():
        n, src, dest = map(int, re.match(pat2, line).groups())
        tmp = list()
        for i in range(n):
            stacksA[dest - 1].appendleft(stacksA[src - 1].popleft())
            tmp.append(stacksB[src - 1].popleft())
        stacksB[dest - 1].extendleft(reversed(tmp))

print(f'part A: {"".join(d[0] for d in stacksA)}')
print(f'part B: {"".join(d[0] for d in stacksB)}')
