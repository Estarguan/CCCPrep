import sys
input = sys.stdin.readline

n, m, x = map(int, input().strip().split())
if x < m*n:
    print(f":blobsob:\n{m*n-x}")
else:
    print(":poggies:")
