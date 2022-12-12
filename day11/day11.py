import copy
from functools import partial

f = 'day11/data.txt'

with open(f, 'r') as of:
    monkeys = of.read().strip().split('\n\n')


def parseitems(line) -> list:
    # worry level per item
    x = line.split(':')[-1].strip()
    return [int(y) for y in x.split(', ')]


def square(x):
    return x * x


def scale(x, n):
    return x * n


def shift(x, n):
    return x + n


def parseop(line) -> callable:
    # how worry changes upon inspection
    n = line.split()[-1]
    op = line.split()[-2]
    if n == 'old':
        return square
    elif op == '+':
        return partial(shift, n=int(n))
    elif op == '*':
        return partial(scale, n=int(n))
    else:
        raise NotImplementedError


def divisor(line) -> int:
    # worry -> decision
    return int(line.split()[-1].strip())


def parsetarget(lines_) -> dict:
    iftrue, iffalse = (int(l.strip().split()[-1]) for l in lines_)
    return dict(monktrue=iftrue, monkfalse=iffalse)


def selection(x, div, monktrue, monkfalse):
    if not (x % div):
        return monktrue
    return monkfalse


def monkey_business(counts: dict):
    vals = sorted(list(counts.values()))
    return vals[-1] * vals[-2]


state = dict()
for i, text in enumerate(monkeys):
    _, itm, oper, test, if1, if0 = text.split('\n')
    state[i] = dict(
        items=parseitems(itm),
        func=parseop(oper),
        divisor=divisor(test),
        test=partial(selection, div=divisor(test), **parsetarget([if1, if0])),
    )
initial = copy.deepcopy(state)

# after inspection but before test, worry = worry // 3
# inspect and throw each item in order
# count number of inspections over 20 rounds

nmonk = len(state)
inspections = {i: 0 for i in range(nmonk)}
# states = list()
for rd in range(20):
    for m in range(nmonk):
        while state[m]['items']:  # while monkey still has items
            # pull out an item
            worry = state[m]['items'].pop(0)
            # inspect item
            worry = state[m]['func'](worry)
            # print(f'updated to {worry}')
            inspections[m] += 1
            # update worry level again
            worry = worry // 3
            # find monkey to throw to
            target = state[m]['test'](worry)
            # throw
            state[target]['items'].append(worry)

print(f'part A: {monkey_business(inspections)}')

# reset
inspections = {i: 0 for i in range(nmonk)}
state = copy.deepcopy(initial)

# greatest common divisor
divisors = [state[m]['divisor'] for m in range(nmonk)]
denom = 1
for d in divisors:
    denom *= d

for rd in range(10000):
    for m in range(nmonk):
        for worry in state[m]['items']:  # while monkey still has items
            # inspect item
            worry = state[m]['func'](worry)
            inspections[m] += 1
            # find monkey to throw to
            target = state[m]['test'](worry)
            # since all divisors are prime, we can factor them out
            # (not efficient to calculate twice but im lazy)
            if worry > denom:
                worry %= denom
            # throw
            state[target]['items'].append(worry)
        state[m]['items'] = []

print(f'part A: {monkey_business(inspections)}')
