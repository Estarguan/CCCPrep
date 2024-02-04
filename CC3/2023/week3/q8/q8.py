import sys
from collections import deque
input = sys.stdin.readline 

def findFactors(number):
  for i in range(1, int(number**0.5) + 1):
    if number % i == 0:
      if number//i <= m:
        if not vis[i][number//i]:
          q.append([i,number //i])
          vis[i][number//i] = True
      if number // i <= n:
        if not vis[number//i][i]:
          q.append([number//i,i])
          vis[number//i][i] = True

grid = []
n = int(input())
m = int(input())
vis = [[False for i in range(m+1)]for j in range(n+1)]
for i in range(n):
  grid.append(list(map(int,input().split())))


q = deque()
findFactors(grid[0][0])

while q:
  x,y = q.popleft()
  if x == n and y == m:
    print("yes")
    sys.exit()
  else:
    findFactors(grid[x-1][y-1])
print("no")