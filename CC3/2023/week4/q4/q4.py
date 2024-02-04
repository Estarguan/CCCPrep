import sys
from collections import deque
input = sys.stdin.readline 

visited = []
n,m = map(int,input().split())

adj = {}
start = None
end = None
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


grid = []
for i in range(n):
  grid.append(list(input().strip()))

for row in range(len(grid)):
  for col in range(len(grid[row])):
    cell = grid[row][col]
    if cell == "s":
      start = (row, col)
    if cell == "e":
      end = (row, col)
    if cell != "X":
      neighbors = []
      for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != "X":
          neighbors.append((r, c))
      adj[(row, col)] = neighbors

visited = set()
q = deque([(start, 0)])
visited.add(start)

answer = -1
while(q):
  node,distance = q.popleft()
  if node == end:
    answer = distance-1

  if node in adj:
    for neighbour in adj[node]:
      if neighbour not in visited:
        q.append([neighbour,distance+1])
        visited.add(neighbour)

print(answer)

  