import sys
input = sys.stdin.readline

cit = list(map(int, input().split()))

c = [0]
for i in range(4):
    c.append(c[i] + cit[i])

for i in range(5):
    r = []
    for j in range(5):
        dist = c[j] - c[i]
        if (dist<0): dist *= -1
        r.append(dist)
    print(*r)
