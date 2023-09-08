import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans,stk=[1],[a[0]]
for i in range(1,n):
  p = bisect_left(stk,a[i])
  if p:
    ans.append(-p)
  ans.append(p+1)
  stk.insert(p,a[i])
ans.append(-n)
print(len(ans))
for x in ans:
  print(x)