import sys
from collections import deque
input = sys.stdin.readline 

n,m = map(int,input().split())
MM = int(2e5+2)
dis = [(2**31 - 1) for i in range(n+1)]
vis = [False for i in range(n+1)]

def bfs():
  while queue:
    p = queue.popleft()
    for i in range(len(grid[p])):
      if not vis[grid[p][i]]:
        vis[grid[p][i]] = True
        queue.append(grid[p][i])
        if dis[p]+1 < dis[grid[p][i]]:
          dis[grid[p][i]] = dis[p]+1
        
queue = deque()
grid = {}
for i in range(m):
  a,b = map(int,input().split())
  if a not in grid:
    grid[a] = []
  if b not in grid:
    grid[b] = []
  grid[a].append(b)
  grid[b].append(a)

cities = []
k = int(input())
for i in range(k):
  cities.append(int(input()))

for i in cities:
  vis[i] = True
  queue.append(i)

bfs()

print(max(dis[1:]))
