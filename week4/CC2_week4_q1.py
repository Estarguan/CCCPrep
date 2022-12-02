import math
import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(t):
    N = int(input().strip())
    if 0 <= N <= 30:
        print("38")
    elif 30 < N <= 50:
        print("55")
    elif 50 < N <= 100:
        print("73")
    elif 100 < N:
        x = N-100
        print(73 + (math.ceil(x/50) * 24))
