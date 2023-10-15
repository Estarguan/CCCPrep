import sys
input = sys.stdin.readline 

n,h,p = map(int,input().split())

bosses = list(map(int,input().split()))

total = sum(bosses)
ans = (total*p)
bosses.sort()
for i in range(n):
   total -= bosses[i]
   ans = min(h*bosses[i] +  (total-(n-i-1)*bosses[i])*p,ans)
   
print(ans)