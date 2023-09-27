import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
grid = {}
for i in range(m):
  a,b = map(int,input().split())
  if a not in grid:
    grid[a] = []
  grid[a].append(b)



p,q = map(int,input().split())

def dfs(j,k):
  if j == k:
    return True
  try:
    for i in grid[j]:
      if dfs(i,k):
        return True
  except KeyError:
    return

if p in grid and len(grid[p]) != 0:
  if dfs(p,q):
    print("yes")
    sys.exit()
if q in grid and len(grid[q]) != 0:
  if dfs(q,p):
    print("no")
    sys.exit()
print("unknown")  