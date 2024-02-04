import sys
from collections import deque
input = sys.stdin.readline 


minimum = 61
for _ in range(int(input())):
  q = deque()
  col,row = map(int,input().split())
  dis = [[sys.maxsize for i in range(col)]for j in range(row)]
  vis = [[False for i in range(col)]for j in range(row)]

  graph = [[] for i in range(row)]
  for i in range(row):
    r = list(input())
    for j in range((len(r))):
      graph[i].append(r[j])
      if r[j] == "C":
        startx, starty = i,j
        dis[startx][starty] = 0
        q.append((startx,starty))
        vis[startx][starty] = True
      elif r[j] == "W":
        endx,endy = i,j

  while q:
    x,y = q.popleft()

    moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    for movel,mover in moves:
      if 0 <= movel < col and 0 <= mover < row:
        if not vis[movel][mover] and graph[mover][movel] != "X":
          vis[movel][mover] = True

          if dis[x][y]+1 < dis[mover][move]:
            dis[mover][movel] = dis[x][y]+1
          q.append((movel,mover))

  print(dis)    
  print(dis[endx][endy])

  
  # for i in graph:
  #   print("".join(i))
  # print(startx,starty)
  # print(endx,endy)
