import sys
input = sys.stdin.readline 
from collections import deque
n = int(input())
adj = [[]for i in range(n+1)]
for i in range(n):
  adj[i+1] += list(map(int,input().split()))[1:]
dis,vis = [0]*(n+1), [False]*(n+1)
q = deque([1])
mi = float('inf')
while q:
  cur = q.popleft()
  if len(adj[cur]) == 0:
    mi = min(mi,dis[cur])
    for nxt in adj[cur]:
      if not vis[nxt]:
        q.append(nxt)
        vis[nxt] = True
        dis[nxt] = dis[cur]+1
print("Y") if all(vis[1:])else print("N")
print(mi)