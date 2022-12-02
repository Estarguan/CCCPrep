import sys
input = sys.stdin.readline

cases = int(input())
for i in range(cases):
    x, p = map(float , input().split())
    print("{:.2f}".format(x**p))
