import sys
input = sys.stdin.readline 
from collections import deque

keys = set()
n = int(input())

graph = {}
for i in range(n):
  a,b = input().split()
  if a not in graph:
    graph[a] = []
  if b not in graph:
    graph[b] = []
  graph[a].append(b)
  graph[b].append(a)
  keys.add(a)

changed = 0

#while True:
  
# if changed == n:
#   print("Yes")
#   sys.exit()
changeAgain = False
def search(keys,changeAgain,changed,graph):
  q = deque()
  for i in keys:
    if changed == n:
      print("Yes")
      sys.exit()
    if i in keys:
      for j in graph[i]:
      
        if j not in keys:
          #changeAgain = True
          keys = keys - {i}
          keys.add(j)
          changed += 1
          changeAgain = True
          for k in graph[i]:
            if k != j:
              q.append(k)
          #changed += 1
    # if not changeAgain:
    #   print("No")
    #   sys.exit()

  while q:
    if changed == n:
      print("Yes")
      sys.exit()
    cur = q.popleft()
    for i in graph[cur]:
      if i not in keys:
        keys = keys-{cur}
        keys.add(i)
        changed += 1
        changeAgain = True
      for j in graph[cur]:
        if j != i:
          q.append(j)

search(keys,changeAgain,changed,graph)
if changeAgain:
  search(keys,changeAgain,changed,graph)
print("No")