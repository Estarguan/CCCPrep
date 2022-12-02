import sys
input = sys.stdin.readline

ans = 0
N = int(input().strip())
lst1 = list(str(input().strip()))
lst2 = list(str(input().strip()))
for i in range(N):
    if lst1[i] == 'C':
        if lst1[i] == lst2[i]:
            ans += 1
print(ans)
