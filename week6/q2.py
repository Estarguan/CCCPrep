import sys
input = sys.stdin.readline

N = int(input())
set = set()
for i in range(N):
    set.add(input().strip())
print(len(set))
