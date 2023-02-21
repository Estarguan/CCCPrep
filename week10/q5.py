import sys
input = sys.stdin.readline

sum, cnt = 0, 0
lst = []
for _ in range(int(input())):
    lst.append(int(input().strip()))
lst.sort()

for i in range(len(lst)):
    if lst[i] >= sum:
        sum += lst[i]
        cnt += 1
print(cnt)
