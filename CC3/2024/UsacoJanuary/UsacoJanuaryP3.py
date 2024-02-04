import sys
input = sys.stdin.readline

n = int(input())
grass = list(map(int, input().split()))

ans = 0
for i in range(n):
    
    cur = grass[i]
    if cur > 0:
        for j in range(i, n):
            grass[j] -= cur * (j - i + 1)
        ans += cur
    else:
        for j in range(i, n):
            grass[j] += -cur * (j - i + 1)
        ans -= cur
print(ans)