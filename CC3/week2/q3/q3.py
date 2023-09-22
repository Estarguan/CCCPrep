import sys
input = sys.stdin.readline

n,m,r,c = map(int,input().split())
grid = [[0 for i in range(m)]for i in range(n)]
if r == n and c != m and c != 0:
  print("IMPOSSIBLE")
  sys.exit()
elif c == m and r != n and r != 0:
  print("IMPOSSIBLE")
  sys.exit()
for i in range(r):
  for j in range(m):
    grid[i][j] = 'a'
for i in range(n):
  for j in range(c):
    grid[i][j] = 'a'
for i in range(n):
  for j in range(m):
    if grid[i][j] == 0:
        grid[i][j] = 'b'
  if grid[i].count('a') == 0:
    grid[i][0] = 'c'
for i in grid:
  print("".join(i))
