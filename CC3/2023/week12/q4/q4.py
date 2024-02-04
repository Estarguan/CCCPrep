import sys
input = sys.stdin.readline

G,P = int(input()),int(input())
p = [i for i in range(G+1)]
ans = 0

def find(d):
  if d != p[d]:
    p[d] = find(p[d])
  return p[d]

for i in range(P):
  g = int(input())
  rt = find(g)
  if rt != 0:
    p[rt] = find(rt-1)
    ans += 1
  else:
    break
print(ans)