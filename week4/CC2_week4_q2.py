import sys
input = sys.stdin.readline

t = int(input().strip())
list = []
for i in range(t):
    N = int(input().strip())
    if N >= 315:
        list.append("N")
    elif N <= 45:
        list.append("N")
    elif 45 < N <= 135:
        list.append("E")
    elif 136 < N <= 225:
        list.append("S")
    else:
        list.append("W")
for i in list:
    print(i)
