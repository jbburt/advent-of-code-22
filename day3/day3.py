from functools import reduce

f = 'day3/data.txt'

with open(f, 'r') as of:
    # elf rucksacks
    sacks = of.read().rstrip('\n').split('\n')

nsacks = len(sacks)

# priority assigned to each item
priority = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# two compartments per sack -> first/second half of elements
# find priority of compartmentally-overlapping item(s)
total = 0
for sack in sacks:
    n = len(sack)
    intersect = set(sack[:n // 2]).intersection(set(sack[n // 2:]))
    total += sum(map(lambda c: priority.find(c), intersect))
print(f'part A: {total}')

# elves are in consecutive groups of 3; "badge" is singular shared item
sets = [set(sack) for sack in sacks]
badges = [
    reduce(lambda a, b: a & b, sets[i:i + 3]) for i in range(0, nsacks, 3)]
total2 = sum(map(lambda x: priority.find(x.pop()), badges))
print(f'part B: {total2}')
