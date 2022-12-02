f = 'day2/data.txt'

with open(f, 'r') as of:
    content = of.read()

content = content.replace(
    'A', '0').replace('X', '0').replace(
    'B', '1').replace('Y', '1').replace(
    'C', '2').replace('Z', '2').replace(
    '\n', ' ').replace(' ', '')

content = list(map(int, content))

n = len(content)

outcomes = [
    [4, 1, 7],
    [8, 5, 2],
    [3, 9, 6]
]

# part A
score = 0
for i in range(0, n, 2):
    other, self = content[i:i + 2]
    score += outcomes[self][other]
print(score)

# part B
score = 0
for i in range(0, n, 2):
    other, outcome = content[i:i + 2]
    self = (((other + 2) % 3) + outcome) % 3
    score += outcomes[self][other]
print(score)
