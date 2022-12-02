import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
lst = [set() for i in range(N)]
for i in range(Q):
    x = input().split()
    if x[0] == "1":
        print(1) if x[2] in lst[int(x[1])-1] else print(0)
    else:
        lst[int(x[1])-1].add(x[2])
