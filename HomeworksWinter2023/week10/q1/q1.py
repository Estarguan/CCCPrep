n,k = map(int,input().split())
walk =0
sections = list(input())
for i in range(n):
  if sections[i] == 'U':
    if k >= 1:
      k-=1
    if k == 0:
      walk += 1 
  elif sections[i] == 'D':
    k += 1
  elif sections[i] == 'F':
    if k == 0:
      walk += 1
print(walk)
