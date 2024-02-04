import sys
input = sys.stdin.readline 

n = int(input())
a = [list(map(int,input().split())) for i in range(n)]

def f(x):
  tot = 0
  for p,w,d in a:
    if x < p-d: tot += w * (p - d -x)
    if x > p+d: tot += w * (x-p-d)
  return tot

lo, hi = 0, int(1e9)
while lo < hi:
  mid = (lo+hi)//2
  if f(mid) < f(mid+1): hi = mid
  else: lo = mid+1

print(f(lo))