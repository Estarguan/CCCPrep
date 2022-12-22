import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int,input().strip().split())
    cows = list(input().strip())
    count = 0
    if k == 0:
        print(cows)
        continue

    print(cows)
