import sys
input = sys.stdin.readline

n,m,r,c = map(int,input().split())
grid = [['a' for i in range(m)]for i in range(n)]
if r == n and c != m and c != 0:
  print("IMPOSSIBLE")
  sys.exit()
elif c == m and r != n and r != 0:
  print("IMPOSSIBLE")
  sys.exit()

for i in range(r,n):
  grid[i][-1] = chr(ord(grid[i][0])+1)
for i in range(c,m):
  grid[n-1][i]= chr(ord(grid[0][i])+1)
if r != n and c == 0:
  grid[-1][-1] = chr(ord(grid[-1][-1])+1)


for i in grid:
  print("".join(i))