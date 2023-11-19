import sys
from collections import deque
input = sys.stdin.readline 

n, m = map(int,input().split())
graph = {}
edges = []

for i in range(1,n+1):
  graph[i] = []

for i in range(m):
  v1,v2 = map(int,input().split())
  graph[v1].append(v2)
  edges.append((v1,v2))

def bfs(removeEdge):
  v, e = removeEdge

  graph[v].remove(e)

  vis = [False]*(n+1)
  q = deque()
  q.append(1)
  vis[1] = True

  while q:
    cur = q.popleft()
    for node in graph[cur]:
      if node == n:
        return True
      else:
        if not vis[node]:
          vis[node] = True
          q.append(node)

  graph[v].append(e)
  return False
  

for i in range(m):
  if bfs(edges[i]):
    print("YES")
  else:
    print("NO")
