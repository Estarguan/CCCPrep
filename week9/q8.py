import sys
input = sys.stdin.readline

cnt = 0
X = int(input())
tog = [input().strip().split() for i in range(X)]
Y = int(input())
untog = [input().strip().split() for i in range(Y)]
d = {}
for i in range(int(input())):
    a, b, c = input().strip().split()
    d[a], d[b], d[c] = i, i, i
for a, b in tog:
    cnt += d[a] != d[b]
for a, b in untog:
    cnt += d[a] == d[b]
print(cnt)
