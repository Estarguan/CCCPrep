import sys
input = sys.stdin.readline

t = int(input().strip())
lst = []
cnt, sum = 0,0
c = int(input().strip())
for i in range(c):
    lst.append(int(input().strip()))

lst.sort()
for i in range(c):
    if lst[i] + sum <= t:
        sum += lst[i]
        cnt += 1
    elif lst[i] + sum >= t:
        break
print(cnt)
