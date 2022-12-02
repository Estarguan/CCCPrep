import sys
input = sys.stdin.readline

n = int(input().strip())
lst = []

for i in range(n):
    num = int(input().strip())
    if num != 0:
        lst.append(num)
    else:
        lst.pop()
print(sum(lst))
