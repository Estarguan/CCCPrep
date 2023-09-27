import sys
<<<<<<< HEAD
input = sys.stdin.readline 

x,y = map(int,input().split())

visited = []
paths = []
nodes = []
if x > y:
  print(x-y)
  sys.exit()
def dfs(node,len):
  for i in range(3):
    if i == 0:
      node += 1

      if node < y:
        len += 1
        dfs(node,len)
      elif node == y:
        paths.append(len)
        break
      node -= 1
    elif i == 1:
      node *= 2
      if node < y:
        len += 1
        dfs(node,len)
      elif node == y:
        paths.append(len)
      node /= 2
      node = int(node)
    elif i == 2:
      node -= 1
      if node < y:
        len += 1
        dfs(node,len)
      elif node == y:
        paths.append(len)
      node += 1
        
dfs(x,0)
print(min(paths))
=======
from collections import deque
input = sys.stdin.readline

MM = int(2e5+2)
x,y = map(int, input().split())
dis = [0 for i in range(MM)]
vis = [False for i in range(MM)]
q = deque()

q.append(x)
vis[x] = 1
dis[x] = 0 
while q:
    cur = q.popleft()
    
    moves = [cur-1, cur+1, cur*2]
    for move in moves:
        if move == y:
            if dis[cur]+1 < dis[move]:
                dis[move] = dis[cur]+1
        if 0 < move < MM and not vis[move]:
            vis[move] = True
            dis[move] = dis[cur] + 1
            q.append(move)
print(dis[y])
>>>>>>> a4675a80e3dd06888fba356c0b2a52efe29a5f7d
