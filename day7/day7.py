f = 'day7/data.txt'

with open(f, 'r') as of:
    lines = of.read().strip().split('\n')


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.id = id(self)
        self.parent = parent
        self.children = dict()
        self.files = dict()

    def getsize(self):
        mysize = self.filesize()

        if not len(self.children):
            return mysize
        else:
            mysize += sum(c.getsize() for c in self.children.values())
        return mysize

    def filesize(self):
        if len(self.files):
            return sum(self.files.values())
        return 0

    def cd(self, dirname):
        if dirname == '..':
            return self.parent
        if dirname not in self.children:
            self.add_child(dirname)
        return self.children[dirname]

    def add_child(self, dirname):
        print(dirname)
        self.children[dirname] = Dir(dirname, self)

    def add_file(self, filesize, filename):
        self.files[filename] = int(filesize)


head = Dir('/', None)
currdir = head
i = 1

while i < len(lines):
    line = lines[i]
    if line.startswith('$'):  # line contains command
        parts = line[2:].split()
        if len(parts) == 1:
            assert parts[0] == 'ls'
        else:
            assert len(parts) == 2 and parts[0] == 'cd'
            currdir = currdir.cd(parts[1])
    else:  # line contains resource
        if line.startswith('dir'):
            newdir = line.split()[-1]
            if newdir not in currdir.children:
                newnode = Dir(newdir, currdir)
                currdir.children[newdir] = newnode
        else:
            currdir.add_file(*line.split())
    i += 1

# determine the total size of each directory
queue = [head, currdir]
visited = dict()
while queue:
    nextdir = queue.pop()
    if nextdir.id in visited:
        continue
    else:
        print(nextdir.name, nextdir.getsize())
    if len(nextdir.children):
        for name, node in nextdir.children.items():
            if node.id != id(nextdir) and node.id not in visited:
                queue.append(node)
    if nextdir.parent is not None:
        for name, node in nextdir.parent.children.items():
            if node.id != id(nextdir) and node.id not in visited:
                queue.append(node)
    visited[nextdir.id] = nextdir.getsize()

total = 0
for memloc, size in visited.items():
    if size <= 100000:
        total += size
print(f'part A: {total}')

# find directory to delete to run the update
total_space = 70000000
req_space = total_space - 30000000
curr_space = head.getsize()
delta = curr_space - req_space

partB = float('inf')
for size in visited.values():
    if delta <= size < partB:
        partB = size
print(f'part B: {partB}')
