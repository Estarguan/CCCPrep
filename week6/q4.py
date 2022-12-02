import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
tot = N

for i in range(K):
    tot += N*10
    N *= 10
print(tot)
