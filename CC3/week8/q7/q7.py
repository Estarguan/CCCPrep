#This code is written with bfs
"""
apparently in a tree
the shortest distance to reach all nodes without returing to the root node
is just 2 * (# of edges) - (distance of longest path from root)
but for a weighted graph
its
2 * (sum of weight of all edges) - (weighted distance of longest path from root)
"""


import sys
from collections import deque
input = sys.stdin.readline 

n = int(input())
graph = ['']*(n+1)
tot = 0

for i in range(n):
  a,b,c = map(int,input().split())
  graph[a] += str(b)+ ' ' + str(c) + ','
  graph[b] += str(a) + ' ' + str(c) + ','
  tot += c

print(graph)

dis = [-1] * (n+1)
q = deque()
dis[0] = 0
q.append(0)

while q:
  cur = q.popleft()
  for s in graph[cur].split(','):
    if len(s) == 0:
      continue
    nxt,w = map(int,s.split())
    if dis[nxt] == -1:
      dis[nxt] = dis[cur] + w
      q.append(nxt)
print(2*tot - max(dis))