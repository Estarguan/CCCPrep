import sys
input = sys.stdin.readline

count = 0

n = int(input())
tog = []
for i in range(n):
    tog.append(input().split())
n = int(input())
untog = []
for i in range(n):
    untog.append(input().split())
g = int(input())
groups = {}
for x in range(g):
    for y in input().split():
        groups[y] = x+1

for i in tog:
    if groups[i[0]] != groups[i[1]]:
        count += 1
for i in untog:
    if groups[i[0]] == groups[i[1]]:
        count += 1
print(count)