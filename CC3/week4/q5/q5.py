import sys
from collections import deque
input = sys.stdin.readline 

graph = {}
bridge = list(input().strip())
edges = 1


def bfs(removeKey,removeEdge):
  graph[removeKey].pop(removeEdge)
  visited = [False for i in range(26)] 
  q = deque('A')
  while q:
    node = q.popleft()
    if node == "B":
      return True 
    else:
      for edge in graph[node]:
        if not visited[ord(edge)-65]:
          q.append(edge)
          visited[ord(edge)-65] = True
  return False



while (bridge != ["*","*"]):
  edges += 1
  l,r = bridge[0],bridge[1]

  if l not in graph:
    graph[l] = []
  if r not in graph:
    graph[r] = []
  graph[l].append(r)
  graph[r].append(l)
  bridge = list(input().strip())


discon = set()
for i in graph.keys():
  for j in range(len(graph[i])):
    temp = graph[i][j]

    if not bfs(i,j):
      discon.add((i,temp))

    graph[i].insert(j,temp)

for i in discon:
  print("".join(i))
print("There are", len(discon),"disconnecting roads.")