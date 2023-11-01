import sys
from collections import deque
input = sys.stdin.readline 

n, m = map(int,input().split())
c = [0] + list(map(int,input().split()))
adj = [[] for i in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  adj[u].append(v)
  adj[v].append(u)
d1,d2 = [[] for i in range(n+1)] , [[] for i in range(n+1)]

def bfs(st,d):
  dis = [-1] * ( n+1)
  q , dis[st] = deque([st]),0
  while q:
    u = q.popleft()
    if len(d[c[u]]) < 2: d[c[u]].append((u,dis[u]))
    for k in adj[u]:
      if dis[k] == -1:
        q.append(k)
        dis[k] = dis[u]+1

bfs(1,d1)
bfs(n,d2)
ans = float('inf')
for i in range(1,n+1):
  for u, du in d1[i]:
    for k,dv in d2[i]:
      if u != k: ans = min(ans,du+dv)

print(ans if ans!= float('inf') else -1)
