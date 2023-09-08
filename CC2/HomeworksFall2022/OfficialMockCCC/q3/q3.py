import sys
input = sys.stdin.readline

n,k,m = map(int, input().strip().split())

a = list(map(int,input().strip().split()))
b = list(map(int, input().strip().split()))
cnt = 0

dicb = {}
for i in range(n):
    dicb[b[i]] = i
for i in range(n):
    needed = m-a[i]
    if needed in dicb.keys():
        if abs(dicb[needed]-i) >= k:
            cnt += 1
print(cnt)
