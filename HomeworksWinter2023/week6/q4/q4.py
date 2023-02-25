import sys
input = sys.stdin.readline 

n = int(input())
a = list(map(int,input().split()))
memo = [[0]*n for i in range(n)]
ans = [float('inf')] * (n+1)
ans[1] = 0
for len in range(2,n+1):
    L,R = 0,len-1
    while R < n:
        memo[L][R] = abs(a[L]-a[R]) + memo[L+1][R-1]
        ans[len] = min(ans[len],memo[L][R])
        L,R = L+1,R+1
        print(L,R)
for i in range(1,n+1):
    print(ans[i], end = ' ')
