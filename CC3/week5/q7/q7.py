import sys
from collections import deque
input = sys.stdin.readline 

def walking():
  q = deque([start])
  vis = set()
  vis.add(start)
  dist = {}
  dist[start] = 0
  while(q):
    cur = q.popleft()
    if cur == end:
      return dist[cur]
    for a,b in dir:
      nr,nc = a+cur[0],b+cur[1]
      if 0<=nr<r and 0<=nc<c and (nr,nc) not in vis:
        if g[nr][nc] == "O":
          q.append((nr,nc))
          vis.add((nr,nc))
          dist[(nr,nc)]= dist[cur] + 1

def teleportation():
  q = deque([start])
  vis = set()
  dist = {}
  dist[start] = 0
  while q:
    cur = q.popleft()
    if cur in tps:
        return dist[cur]
    
    for a,b in dir:
      nr,nc = a+cur[0],b+cur[1]
      if 0<=nr<r and 0<=nc<c and (nr,nc) not in vis:
        if g[nr][nc] == "O":
          q.append((nr,nc))
          vis.add((nr,nc))
          dist[(nr,nc)]= dist[cur] + 1

r,c = map(int,input().split())
start = tuple(list(map(int, input().split())))
end = tuple(list(map(int, input().split())))

g = [list(input().strip())for i in range(r)]
teleporters = int(input())
tps = set()
for i in range(teleporters):
  tps.add(tuple(list(map(int, input().split()))))

dir = [(-1,0),(1,0),(0,-1),(0,1)]

print(walking()-teleportation())
  
