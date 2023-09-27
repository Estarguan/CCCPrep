import sys
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