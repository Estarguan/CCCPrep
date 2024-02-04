#https://dmoj.ca/problem/ccc16s3
import sys
input = sys.stdin.readline 
sys.setrecursionlimit(int(1e5)+10)

n,m = map(int,input().split())
pho = [False] * n
for rt in list(map(int,input().split())):
  pho[rt] = True
adj = [[] for i in range(n)]
for i in range(n-1):
  u,v = map(int,input().split())
  adj[u].append(v)
  adj[v].append(u)

#pre makes sure you dont go back to the parent node
#this is to remove and node that has no pho shop after it because you don't need it
def dfs1(u,pre):
  for v in adj[u]:
    if v != pre:
      dfs1(v,u)
      if pho[v]:
        pho[u] = True


def dfs2(u,pre,dis):
  global far, dia
  if dis > dia:
    dia,far = dis,u
  for v in adj[u]:
    if v != pre and pho[v]:
      dfs2(v,u,dis+1)

dfs1(rt,-1)
far,dia = 0,0
dfs2(rt,-1,0)
dfs2(far,-1,0)


E=sum(pho)-1

print(2*E-dia)