import sys
input = sys.stdin.readline

for i in range(int(input().strip())):
    n, c = input().split()
    print(c * int(n))
