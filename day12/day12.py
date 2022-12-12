import heapq

f = 'day12/data.txt'

with open(f, 'r') as of:
    grid = [list(l) for l in of.read().strip().split('\n')]

# convert to ints and store start/end locations
start = end = None
for i, row in enumerate(grid):
    for j, value in enumerate(row):
        if value == 'S':
            grid[i][j] = 0
            start = (i, j)
        elif value == 'E':
            grid[i][j] = 26
            end = (i, j)
        else:
            grid[i][j] = int(ord(value) - ord('a'))

# turn this into a graph
nrow = len(grid)
ncol = len(grid[0])
nodes = [(i, j) for i in range(nrow) for j in range(ncol)]

graph = {node: list() for node in nodes}
for i, j in graph.keys():
    height = grid[i][j]
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        node2 = (i + di, j + dj)
        if node2 in graph:
            i2, j2 = node2
            if grid[i2][j2] <= (height + 1):
                graph[(i, j)].append(node2)


# use dikjstra w help from gpt3
def dijkstra(evalfn):
    # initialize all the distances in the graph to infinity
    distances = {}
    paths = {}
    for node in graph:
        paths[node] = []
        distances[node] = float('inf')

    # update starting node
    distances[start] = 0
    paths[start] = [start]

    # create an empty set to store the nodes we have visited
    visited = set()

    # create a heap to store the nodes we need to visit
    heap = []

    # add the starting node to the heap
    heapq.heappush(heap, (0, start))

    # loop until the heap is empty
    while len(heap) > 0:

        # pop the node from the heap
        (distance, node) = heapq.heappop(heap)

        # if the node has not been visited yet
        if node not in visited:

            # mark it as visited
            visited.add(node)

            # if the node is the end, exit
            if evalfn(node):
                return distances, node

            # if not, loop through its neighbors
            for neighbor in graph[node]:

                # calculate the new distance to the neighbor
                new_distance = distance + 1

                # if the new distance is shorter than the current distance
                if new_distance < distances[neighbor]:
                    # update
                    distances[neighbor] = new_distance
                    paths[neighbor] = paths[node] + [neighbor]

                    # add the neighbor to the heap
                    heapq.heappush(heap, (new_distance, neighbor))
    return distances, None


dists1, _ = dijkstra(lambda x: x == end)
print(f'part A: {dists1[end]}')

# find fastest path down from top
tmp = start
start = end

graph = {node: list() for node in nodes}
for i, j in graph.keys():
    height = grid[i][j]
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        node2 = (i + di, j + dj)
        if node2 in graph:
            i2, j2 = node2
            # change criterion s.t. we only traverse down climable paths
            if grid[i2][j2] >= height - 1:
                graph[(i, j)].append(node2)

dists2, base = dijkstra(lambda x: grid[x[0]][x[1]] == 0)
print(f'part B: {dists2[base]}')
