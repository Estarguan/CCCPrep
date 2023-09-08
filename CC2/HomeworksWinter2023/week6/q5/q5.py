import sys
from itertools import combinations
input = sys.stdin.readline

n, t = map(int,input().split())
a = [int(input()) for i in range(n)]

ans = float('inf')
for len in range(1,len(a)+1):
    for x in combinations(a,len):
        s = sum(x)
        if s >= t:
            ans = min(ans,s-t)
print(ans)