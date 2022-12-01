import heapq

f = 'day1/data.txt'

maxcals = 0
curr_sum = 0
with open(f, 'r') as of:
    lines = of.read().split('\n')

totals = list()

# part A
for line in lines:
    if not line:
        # compare to current maximum
        totals.append(curr_sum)
        if curr_sum > maxcals:
            maxcals = curr_sum
        curr_sum = 0
    else:
        curr_sum += int(line)
print(f'problem 1: {maxcals}')

# part B
print(f'problem 2: {sum(heapq.nlargest(3, totals))}')
