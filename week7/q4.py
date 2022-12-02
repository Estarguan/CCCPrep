import sys
input = sys.stdin.readline

q = input().strip()
max = 0
for x in range(len(q)):
    for y in range(len(q)+1):
        n = q[x:y]
        if n == n[::-1]:
            if len(n) > max:
                max = len(n)
print(max)
