import sys
from collections import deque
input = sys.stdin.readline 

n,m = map(int,input().split())
grid = {}
for i in range(m):
  a,b = map(int,input().split())
  if a not in grid:
    grid[a] = []
  if b not in grid:
    grid[b] = []
  grid[a].append(b)
p,q = map(int,input().split())

if p in grid:

  queue = deque()
  queue.append(p)
  vis = [False]*(n+1)

  while queue:
    j = queue.popleft()
    found = False
    for i in grid[j]:
      if i == q:
        found = True
        break
      if not vis[i]:
        vis[i] = True
        queue.append(i)
    if found:
      print("yes")
      sys.exit()


if q in grid:
  queue = deque()
  queue.append(q)
  vis = [False]*(n+1)

  while queue:
    j = queue.popleft()
    found = False
    for i in grid[j]:
      if i == p:
        found = True
        break
      if not vis[i]:
        vis[i] = True
        queue.append(i)
    if found:
      print("no")
      sys.exit()

print("unknown")