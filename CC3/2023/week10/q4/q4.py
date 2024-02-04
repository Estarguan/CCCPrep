import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
  a,b,c,d = map(int,input().split())
  adj[a].append((b,[d,c]))
  adj[b].append((a,[d,c]))

dis = [[float('inf'),float('inf')] for i in range(n+1)]
vis = [False] * (n+1)

dis[1] = [0,0]
for k in range(n):
  mi,u = [float('inf'),float('inf')],-1
  for i in range(1,n+1):
    if not vis[i] and dis[i] < mi:
      mi, u = dis[i],i
  vis[u] = True
  for v,w in adj[u]:
    if not vis[v] and dis[v]>w:
      dis[v] = w 
  
dangerous, cost = 0,0
for x,y in dis[1:]:
  dangerous += x
  cost += y
print(dangerous,cost)