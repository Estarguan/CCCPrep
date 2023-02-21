import sys
from collections import defaultdict
n,m = map(int,input().split())
if n == 0:
  print(-1)
  sys.exit()
banned = []
for i in range(m):
    banned.append(int(input()))
routes = defaultdict(list)
for i in range(n):
    a, b = map(int, input().strip().split())
    routes[a].append(b)
    routes[b].append(a)
visited = set()
visited.add(1)
shortest = 9223372036854775807
count = 0

def dfs(currentroute, visited):
  if currentroute == 727:
    return 0
  if currentroute in banned:
    return -1

  if currentroute not in routes:
    return -1

  visited.add(currentroute)

  shortest = 9223372036854775807
  for i in routes[currentroute]:
    if i in visited:
      continue
    ans = dfs(i, visited.copy())
    if ans == -1:
      continue
    shortest = min(shortest, 1 + ans)

  return shortest



if 1 in banned or 727 in banned:
  print(-1)
else:
  ans = dfs(1, set())
  if ans == 9223372036854775807:
    print(-1)
  else:
    print(ans)