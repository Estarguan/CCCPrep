import sys
sys.stdin.readline

P = int(input().strip())
N = int(input().strip())
R = int(input().strip())
count = 0
pre = N
while (N<=P):
    pre = pre*R
    N += pre
    count += 1
print(count)
