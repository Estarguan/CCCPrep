import sys
input = sys.stdin.readline 

n,k = map(int,input().split())

lst = list(input().strip())
index = []
for i in range(len(lst)):
  if lst[i] == 0: continue
  if lst[i] == '1':
    if i+1 < n and lst[i+1] == '1':
      lst[i] = '0'
    else:
      index.append(i)
  
ans = len(index)
gap = []
for i in range(1,len(index)):
  gap.append(index[i] - index[i-1]-1)
gap.sort()
for x in gap:
  if k >= x:
    k -= x
    ans -= 1

if k > 0:
  ans = max(ans,1)
print(ans)