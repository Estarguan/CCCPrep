import sys
input = sys.stdin.readline

N, M, Y = map(float, input().split())
for i in range(int(Y+1)):
    print(i, "{:.2f}".format(N))
    N += N*(M/100)
