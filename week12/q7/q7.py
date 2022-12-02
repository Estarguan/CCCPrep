import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
petals = list(map(int, input().strip().split(" ")))
for i in range(n):
    for j in range(i,n+1):
        if petals[i:j]:
            avg = sum(petals[i:j])/(j-i)
            if avg in petals[i:j]:
                cnt += 1
print(cnt)
