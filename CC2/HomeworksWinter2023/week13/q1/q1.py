import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    ans = 0
    n,s = map(int,input().split())
    want = int((n+1)/2 * n - s)
    count = 0
    for j in range(1, int((want+1)//2)):
        if max(j, want-j) <= n:
            count += 1
    print(count)
