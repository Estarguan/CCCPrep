import sys 
input = sys.stdin.readline 

from collections import deque 

rows,cols = map(int,input().split())
arr = [["*"] * cols for i in range(rows)]
damR, dramC = -1,-1
qFlood = deque()

distFlood = [[float('inf')]* cols for i in range(rows)]
visFlood = [[False]*cols for i in range(rows)]
q= deque()

#always make the distance inf minus the starting point. Idk why but we always do this and sometimes it doesn't work otherwise
dist = [[float('inf')] * cols for i in range(rows)]
vis = [[False]*cols for i in range(rows)] 
for i in range(rows):
  line = input()
  for j in range(cols):
    arr[i][j] = line[j]
    if line[j] == 'D':
      damR,damC = i,j
    if line[j] == '*':
      qFlood.append([i,j])
      visFlood[i][j] = True
      distFlood[i][j] = 0
    if line[j] == "S":
      q.append([i,j])
      vis[i][j] = True
      dist[i][j] = 0
dir = [[0,1],[1,0],[-1,0],[0,-1]]

#Basically this finds the minimum time it takes a certain tile to be flooded
#For example one tile may get flooded in 10 seconds from water source 1
#but gets flooded in only 4 secsonds from water source 2 so we need to check it with bfs
while qFlood:
  curR,curC = map(int,qFlood.popleft())
  for r,c in dir:
    if 0<= curR+r < rows and 0 <= curC + c < cols:
      if not visFlood[curR+r][curC+c] and (arr[curR+r][curC+c] == "." or arr[curR+r][curC+c] == "S"):
        visFlood[curR+r][curC+c] = True
        distFlood[curR+r][curC+c] = distFlood[curR][curC]+1
        qFlood.append([curR+r,curC+c])

while q:
  curR, curC = map(int,q.popleft())
  for r,c in dir:
    if 0<= curR+r < rows and 0<= curC + c<cols:
      #distFlood[curR+r][curC+c] > (dist[curR][curC]+1)
      #This line checks to see if you can get to position curR+1,curC+c faster or does the flood get there faster
      if arr[curR + r][curC + c] != 'X' and distFlood[curR+r][curC+c] > (dist[curR][curC]+1) and not vis[curR+r][curC+c]:
        vis[curR+r][curC+c] = True 
        dist[curR+r][curC+c] = dist[curR][curC] + 1
        q.append([curR+r,curC+c])

if vis[damR][damC]:
  print(dist[damR][damC])
else:
  print("KAKTUS")