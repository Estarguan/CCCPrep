import sys
input = sys.stdin.readline 

n,m,a,b = map(int,input().split())
grid = {}
for i in range(n):
  grid[i+1] = []

for i in range(m):
  l,r = map(int,input().split())
  grid[l].append(r)
  grid[r].append(l)
if a ==b:
  print("GO SHAHIR!")
  sys.exit()
visited = [a]
queue = [a]
found = False
while queue:
  m = queue.pop(0)

  for node in grid[m]:
    if node == b:
      found = True
      break
    if node not in visited:
      visited.append(node)
      queue.append(node)
if found:
  print("GO SHAHIR!")
else:
  print("NO SHAHIR!")
