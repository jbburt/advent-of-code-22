from decimal import Decimal

from scipy.optimize import root

f = 'day21/data.txt'

with open(f, 'r') as of:
    content = of.read().strip()

d = dict()
string = ''
for line in content.split('\n'):
    monkey, etc = line.split(': ')
    if monkey == 'root':
        string = etc
    if etc.isnumeric():
        d[monkey] = Decimal(etc)
    else:
        m1, op, m2 = etc.strip().split()
        e = dict(monkeys=[m1, m2], op=op)
        d[monkey] = e

n = 0
while True:
    n += 1
    try:
        solution = eval(string)
        break
    except NameError:
        for elem in string.split():
            if elem in d:
                if isinstance(d[elem], Decimal):
                    string = string.replace(elem, str(d[elem]))
                else:
                    m1, m2 = d[elem]['monkeys']
                    op = d[elem]['op']
                    string = string.replace(elem, f" ( {m1} {op} {m2} ) ")
print(f'p1: {int(solution)}')

for line in content.split('\n'):
    monkey, etc = line.split(': ')
    if monkey == 'root':
        string = etc.replace(d['root']['op'], '=')
        break

d['humn'] = 'x'
for i in range(n):
    for elem in string.split():
        if elem in d:
            if d[elem] == 'x' or isinstance(d[elem], Decimal):
                string = string.replace(elem, str(d[elem]))
            else:
                m1, m2 = d[elem]['monkeys']
                op = d[elem]['op']
                string = string.replace(elem, f" ( {m1} {op} {m2} ) ")

left, right = string.split(' = ')
init = 3759515934982  # informed by earlier attempt lol


def fn(x):
    global left, right
    return [eval(left.replace('x', str(x[0]))) - eval(
        right.replace('x', str(x[0])))]


# solve for function root
res = root(fn, x0=[init], tol=1e-10)
ans = int(res.x[0])

print(f'p2: {ans}')
