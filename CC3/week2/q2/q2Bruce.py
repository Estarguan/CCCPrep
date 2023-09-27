import sys
input = sys.stdin.readline 

n = int(input())
a = list(map(int,input().split()))
ans = [float('inf')]*(n+1)
for i in range(n):
  val,l,r = 0,i,i
  while 0 <= l and r < n:
    val += abs(a[l]-a[r])
    ans[r-l+1] = min(ans[r-l+1],val)
    l,r = l-1,r+1
  val,l,r = 0,i,i+1
  while 0 <= l and r < n:
    val += abs(a[l]-a[r])
    ans[r-l+1] = min(ans[r-l+1],val)
    l,r = l-1,r+1
print(*ans[1:n+1])