import sys
input = sys.stdin.readline 

n,h,p = map(int,input().split())
hp = list(map(int,input().split()))
ans = 0
if h < p:
  ans = h*max(hp)
elif:
  